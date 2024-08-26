import json
import re
import requests
import pandas as pd
from io import StringIO
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError

from riverdata.models import AlpineMeadowsGauge


class BaseFetchWeatherData:
    date = None
    time = None
    snow_water_equivalent = None
    snow_depth = None
    precipitation_accumulation = None
    air_temperature = None

    def fetch_data(self):
        try:
            try:
                response = requests.get(self.url)
                response.raise_for_status()  # Check if the response was successful

                data = response.text
                data_lines = data.splitlines()

                start_row = -1
                for i, line in enumerate(data_lines):
                    if line.startswith('20'):
                        start_row = (i - 1)
                        break

                if start_row == -1:
                    raise ValueError('Could not find start row')

                df = pd.read_csv(StringIO('\n'.join(data_lines[start_row:])))

                df = df.fillna({
                    'Snow Water Equivalent (in)': 0,
                    'Snow Depth (in)': 0,
                    'Precipitation Accumulation (in)': 0,
                    'Air Temperature Observed (degF)': 0
                })

                data_list = []
                for _, row in df.iterrows():
                    datetimestamp = row['Date']
                    snow_water_equivalent = row['Snow Water Equivalent (in)']
                    snow_depth = row['Snow Depth (in)']
                    precipitation_accumulation = row['Precipitation Accumulation (in)']
                    air_temperature = row['Air Temperature Observed (degF)']

                    dt = datetime.strptime(datetimestamp, '%Y-%m-%d %H:%M')
                    date = dt.date()
                    time = dt.time()

                    data_list.append({'date': date,
                                      'time': time,
                                      'snow_water_equivalent': snow_water_equivalent,
                                      'snow_depth': snow_depth,
                                      'precipitation_accumulation': precipitation_accumulation,
                                      'air_temperature': air_temperature
                    })

                df = pd.DataFrame(data_list)

                # Sorting here will make the id for the entry non-sequential on the database.
                # data = sorted(combined_data, key=lambda k: (k['date'], k['time']), reverse=True)

                # Sorting here will make the id for the entry sequential on the database.
                df = df.sort_values(by=['date', 'time'], ascending=[True, False])
                self.update_database(df.to_dict(orient='records'))
                return True, f'Successfully fetched Alpine Meadows data.'
            except Exception as e:
                return False, f'Failed to fetch Alpine Meadows data: {e}'

        except requests.exceptions.RequestException as e:
            return False, f'Error fetching Alpine Meadows data: {e}'

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                date=entry['date'],
                time=entry['time'],
                defaults={
                    'snow_water_equivalent': entry['snow_water_equivalent'],
                    'snow_depth': entry['snow_depth'],
                    'precipitation_accumulation': entry['precipitation_accumulation'],
                    'air_temperature': entry['air_temperature'],
                }
            )


class FetchAlpineMeadowsGauge(BaseFetchWeatherData):
    url = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customSingleStationReport/hourly/908:WA:SNTL%7Cid=%22%22%7Cname/-167,0/WTEQ::value,SNWD::value,PREC::value,TOBS::value'
    model = AlpineMeadowsGauge


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetches = [FetchAlpineMeadowsGauge()]
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
