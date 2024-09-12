import pandas as pd

from datetime import datetime, timedelta, timezone
from django.core.management.base import BaseCommand
from django.db.models import Value, DateTimeField

from riverdata.models import GraniteFallsGauge, GraniteFallsPrediction, GraniteFallsForecast


class Command(BaseCommand):
    model = GraniteFallsForecast

    def handle(self, *args, **options):
        try:
            self.clear_database()
            current_datetime = datetime.now(timezone.utc)
            ten_days_ago = current_datetime - timedelta(days=10)

            # granite_falls_observed = list(GraniteFallsGauge.objects.filter(date__gte=ten_days_ago).annotate(
            #     prediction_datetime=Value(None, output_field=DateTimeField())).values('date', 'time',
            #                                                                           'gauge_name', 'stage',))

            granite_falls_observed = list(GraniteFallsGauge.objects.filter(datetime__gte=ten_days_ago).values(
                'datetime',
                'date',
                'time',
                'gauge_name',
                'stage',))

            granite_falls_forecast = list(
                GraniteFallsPrediction.objects.filter(datetime__gt=current_datetime).values('datetime',
                                                                                            'date',
                                                                                            'time',
                                                                                            'gauge1_name',
                                                                                            'gauge1_stage',
                                                                                            'prediction_datetime'))

            observed_df = pd.DataFrame(granite_falls_observed)
            # observed_df['prediction_datetime'] = pd.NaT
            observed_df['prediction_datetime'] = current_datetime

            # observed_df['prediction_datetime'] = pd.to_datetime(observed_df['prediction_datetime'], utc=True)
            # observed_df['prediction_datetime'] = pd.to_datetime(observed_df['prediction_datetime']).dt.tz_localize(
            #     'UTC')

            forecast_df = pd.DataFrame(granite_falls_forecast)

            forecast_df.rename(columns={'gauge1_name': 'gauge_name', 'gauge1_stage': 'stage'}, inplace=True)

            # print(observed_df['prediction_datetime'].dtype)
            # print(forecast_df['prediction_datetime'].dtype)

            merged_df = pd.concat([observed_df, forecast_df], ignore_index=True)

            # print(merged_df)

            self.update_database(merged_df)
            self.stdout.write(self.style.SUCCESS('Successfully combined river data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to combine river data: ' + str(e)))


    def clear_database(self):
        self.model.objects.all().delete()

    def update_database(self, df):
        for _, entry in df.iterrows():
            prediction_datetime = entry['prediction_datetime'] if pd.notna(entry['prediction_datetime']) else None

            self.model.objects.update_or_create(
                datetime=entry['datetime'],
                date=entry['date'],
                time=entry['time'],
                defaults={
                    'gauge_name': entry['gauge_name'],
                    'stage': entry['stage'],
                    'prediction_datetime': prediction_datetime,
                }
            )
