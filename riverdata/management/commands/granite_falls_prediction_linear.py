import joblib
import os
import pandas as pd

from datetime import datetime, timezone
from django.core.management.base import BaseCommand

from riverdata.models import JordanRoadGauge, GraniteFallsPredictionLinear
from robeForecast import settings

model_path = os.path.join(settings.BASE_DIR, 'riverdata', 'model', 'RandomForestRegressorLinear.pkl')
with open(model_path, 'rb') as file:
    rf_model = joblib.load(file)


class Command(BaseCommand):
    model = GraniteFallsPredictionLinear

    def handle(self, *args, **options):
        try:
            # Delete tables entries for reset
            self.model.objects.all().delete()

            current_datetime = datetime.now(timezone.utc)

            jordan_prediction_data = list(JordanRoadGauge.objects.filter(datetime__gt=current_datetime).values(
                'datetime',
                'gauge_name',
                'stage',))

            # df = pd.DataFrame(weather_prediction_data).drop(columns=['datetime', 'date', 'time', 'gauge_name'])
            df = pd.DataFrame(jordan_prediction_data).drop(columns=['datetime', 'gauge_name'])


            df['predicted_value'] = rf_model.predict(df)

            prediction_datetime = datetime.now(timezone.utc)
            df['prediction_datetime'] = prediction_datetime

            df['predicted_value'] = df['predicted_value'].round(2)

            combined_data = df.to_dict('records')

            self.update_database(combined_data, jordan_prediction_data)
            self.stdout.write(self.style.SUCCESS('Successfully predicted Granite Falls linear model.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to predict Granite Falls linear model: ' + str(e)))

    def update_database(self, combined_data, jordan_prediction_data):
        for prediction, original_entry in zip(combined_data, jordan_prediction_data):
            self.model.objects.update_or_create(
                datetime=original_entry['datetime'],
                defaults={
                    'gauge_name': 'Granite Falls',
                    'stage': prediction['predicted_value'],
                    'prediction_datetime': prediction['prediction_datetime'],
                }
            )
