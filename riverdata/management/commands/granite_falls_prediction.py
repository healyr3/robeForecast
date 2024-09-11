import joblib
import os
import pandas as pd

from datetime import datetime
from django.core.management.base import BaseCommand

from riverdata.models import GraniteFallsPrediction, CombinedPredictions
from robeForecast import settings

model_path = os.path.join(settings.BASE_DIR, 'riverdata', 'model', 'RandomForestRegressor.pkl')
with open(model_path, 'rb') as file:
    rf_model = joblib.load(file)


class Command(BaseCommand):
    model = GraniteFallsPrediction

    def handle(self, *args, **options):
        try:
            current_datetime = datetime.now()

            weather_prediction_data = list(CombinedPredictions.objects.filter(date__gt=current_datetime).values('date',
                                                                                                                'time',
                                                                                                                'gauge_name',
                                                                                                                'gauge_stage',
                                                                                                                'sp_temp',
                                                                                                                'sp_rain_3h',
                                                                                                                'sp_snow_3h',
                                                                                                                'ap_temp',
                                                                                                                'ap_rain_3h',
                                                                                                                'ap_snow_3h',
                                                                                                                'am_snow_water_equivalent',
                                                                                                                'am_snow_depth',
                                                                                                                'am_precipitation_accumulation',
                                                                                                                'am_air_temperature'))

            df = pd.DataFrame(weather_prediction_data).drop(columns=['date', 'time', 'gauge_name'])
            df['predicted_value'] = rf_model.predict(df)
            df['predicted_value'] = df['predicted_value'].round(2)
            combined_data = df.to_dict('records')

            self.update_database(combined_data, weather_prediction_data)
            self.stdout.write(self.style.SUCCESS('Successfully combined river data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to combine river data: ' + str(e)))

    def update_database(self, combined_data, weather_prediction_data):
        for prediction, original_entry in zip(combined_data, weather_prediction_data):
            self.model.objects.update_or_create(
                date=original_entry['date'],
                time=original_entry['time'],
                defaults={
                    'sp_temp': original_entry['sp_temp'],
                    'sp_rain_3h': original_entry['sp_rain_3h'],
                    'sp_snow_3h': original_entry['sp_snow_3h'],
                    'ap_temp': original_entry['ap_temp'],
                    'ap_rain_3h': original_entry['ap_rain_3h'],
                    'ap_snow_3h': original_entry['ap_snow_3h'],
                    'am_snow_water_equivalent': original_entry['am_snow_water_equivalent'],
                    'am_snow_depth': original_entry['am_snow_depth'],
                    'am_precipitation_accumulation': original_entry['am_precipitation_accumulation'],
                    'am_air_temperature': original_entry['am_air_temperature'],
                    'gauge2_name': original_entry['gauge_name'],
                    'gauge2_stage': original_entry['gauge_stage'],
                    'gauge1_name': 'Granite Falls',
                    'gauge1_stage': prediction['predicted_value'],
                }
            )
