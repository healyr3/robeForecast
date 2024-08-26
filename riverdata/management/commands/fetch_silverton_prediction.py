import json
import re
import requests
import pandas as pd
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError

from riverdata.models import SilvertonWeatherPrediction


class BaseFetchWeatherData:
    date = None
    time = None
    temp = None
    rain_3h = None

    def fetch_data(self):
        try:
            try:
                response = requests.get(self.url)
                response.raise_for_status()  # Check if the response was successful

                data_dict = json.loads(response.text)

                data_list = []
                for entry in data_dict['list']:
                    datetimestamp = entry['dt_txt']
                    temp = entry['main']['temp']
                    rain_3h = entry.get('rain', {}).get('3h', 0)

                    dt = datetime.strptime(datetimestamp, '%Y-%m-%d %H:%M:%S')
                    date = dt.date()
                    time = dt.time()

                    temp = ((temp - 273.15) * (9/5) + 32)

                    data_list.append({'date': date, 'time': time, 'temp': temp, 'rain_3h': rain_3h})

                df = pd.DataFrame(data_list)

                # Sorting here will make the id for the entry non-sequential on the database.
                # data = sorted(combined_data, key=lambda k: (k['date'], k['time']), reverse=True)

                # Sorting here will make the id for the entry sequential on the database.
                df = df.sort_values(by=['date', 'time'], ascending=[True, False])
                self.update_database(df.to_dict(orient='records'))
                return True, f'Successfully fetched Silverton weather data.'
            except Exception as e:
                return False, f'Failed to fetch Silverton weather data: {e}'

        except requests.exceptions.RequestException as e:
            return False, f'Error fetching Silverton weather data: {e}'

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                date=entry['date'],
                time=entry['time'],
                defaults={
                    'temp': entry['temp'],
                    'rain_3h': entry['rain_3h'],
                }
            )


class FetchSilvertonPrediction(BaseFetchWeatherData):
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat=48.07844&lon=-121.567062&appid=13cdb64b7473084e923d86c390fec22e'
    model = SilvertonWeatherPrediction


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetches = [FetchSilvertonPrediction()]
        a = datetime.now()
        for fetch in fetches:
            success, message = fetch.fetch_data()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))
        b = datetime.now()
        delta = b - a
        print(delta)
