import pandas as pd

from datetime import datetime, timedelta, timezone
from django.core.management.base import BaseCommand
from django.db.models import Value, DateTimeField

from riverdata.models import GraniteFallsGauge, GraniteFallsPrediction, GraniteFallsForecast, GraniteFallsPredictionArchive


class Command(BaseCommand):
    model = GraniteFallsForecast

    def handle(self, *args, **options):
        try:
            # Archive past predictions
            self.archive_predictions()

            # Clear past predictions from the table
            self.clear_database()

            current_datetime = datetime.now(timezone.utc)
            ten_days_ago = current_datetime - timedelta(days=10)

            granite_falls_observed = list(GraniteFallsGauge.objects.filter(datetime__gte=ten_days_ago).values(
                'datetime',
                'gauge_name',
                'stage',))

            granite_falls_forecast = list(
                GraniteFallsPrediction.objects.filter(datetime__gt=current_datetime).values('datetime',
                                                                                            'gauge_B_name',
                                                                                            'gauge_B_stage',
                                                                                            'prediction_datetime'))

            observed_df = pd.DataFrame(granite_falls_observed)

            # Extract the prediction_datetime from the first element on the granite_falls_forecast so that all
            # forecast values use the same prediction_datetime
            if granite_falls_forecast:
                gff_prediction_datetime = granite_falls_forecast[0]['prediction_datetime']
            else:
                gff_prediction_datetime = None

            observed_df['prediction_datetime'] = gff_prediction_datetime

            forecast_df = pd.DataFrame(granite_falls_forecast)

            forecast_df.rename(columns={'gauge_B_name': 'gauge_name', 'gauge_B_stage': 'stage'}, inplace=True)

            merged_df = pd.concat([observed_df, forecast_df], ignore_index=True)

            self.update_database(merged_df)
            self.stdout.write(self.style.SUCCESS('Successfully combined river data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to combine river data: ' + str(e)))

    def archive_predictions(self):
        predictions = self.model.objects.all()
        current_datetime = datetime.now(timezone.utc)
        archive_prediction = []

        for prediction in predictions:
            if prediction.datetime > current_datetime:
                archive_prediction.append(prediction)
        for entry in archive_prediction:
            GraniteFallsPredictionArchive.objects.update_or_create(
                prediction_datetime=entry.prediction_datetime,
                gauge_name=entry.gauge_name,
                stage=entry.stage,
                forecast_datetime=entry.datetime,
            )

    def clear_database(self):
        self.model.objects.all().delete()

    def update_database(self, df):
        for _, entry in df.iterrows():
            prediction_datetime = entry['prediction_datetime'] if pd.notna(entry['prediction_datetime']) else None

            self.model.objects.update_or_create(
                datetime=entry['datetime'],
                defaults={
                    'gauge_name': entry['gauge_name'],
                    'stage': entry['stage'],
                    'prediction_datetime': prediction_datetime,
                }
            )
