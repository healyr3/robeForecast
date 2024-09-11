import pandas as pd

from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

from riverdata.models import GraniteFallsGauge, GraniteFallsPrediction, GraniteFallsForecast


class Command(BaseCommand):
    model = GraniteFallsForecast

    def handle(self, *args, **options):
        try:
            self.clear_database()
            current_datetime = datetime.now()
            ten_days_ago = current_datetime - timedelta(days=10)

            granite_falls_observed = list(GraniteFallsGauge.objects.filter(date__gte=ten_days_ago).values('date',
                                                                                                           'time',
                                                                                                           'gauge_name',
                                                                                                           'stage'))

            granite_falls_forecast = list(
                GraniteFallsPrediction.objects.filter(date__gt=current_datetime).values('date',
                                                                                        'time',
                                                                                        'gauge1_name',
                                                                                        'gauge1_stage'))

            observed_df = pd.DataFrame(granite_falls_observed)
            forecast_df = pd.DataFrame(granite_falls_forecast)

            forecast_df.rename(columns={'gauge1_name': 'gauge_name', 'gauge1_stage': 'stage'}, inplace=True)

            merged_df = pd.merge(observed_df, forecast_df, on=['date', 'time', 'gauge_name', 'stage'], how='outer')

            self.update_database(merged_df)
            self.stdout.write(self.style.SUCCESS('Successfully combined river data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to combine river data: ' + str(e)))


    def clear_database(self):
        self.model.objects.all().delete()

    def update_database(self, df):
        for _, entry in df.iterrows():
            self.model.objects.update_or_create(
                date=entry['date'],
                time=entry['time'],
                defaults={
                    'gauge_name': entry['gauge_name'],
                    'stage': entry['stage'],
                }
            )
