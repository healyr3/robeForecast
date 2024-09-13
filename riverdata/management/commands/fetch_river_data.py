import re
import requests
from datetime import datetime
from django.core.management.base import BaseCommand

from riverdata.models import GraniteFallsGauge, JordanRoadGauge
from .combine_river_data import Command as CombineCommand

class BaseFetchRiverData:
    gauge_name = None
    url = None
    model = None
    def fetch_data(self):
        try:
            # Delete tables entries for reset
            # self.model.objects.all().delete()

            response = requests.get(self.url)
            response.raise_for_status()  # Check if the response was successful

            data = response.text

            datetimestamp = r'<dataDateTime>(.*?)</dataDateTime>'
            stage = r'<stage units="feet">(.*?)</stage>'

            datetime_match = re.findall(datetimestamp, data)
            stage_match = re.findall(stage, data)

            if len(datetime_match) == len(stage_match):
                combined_data = []
                for dt_str, stage_str in zip(datetime_match, stage_match):
                    dt = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M:%SZ')
                    combined_data.append({
                        'gauge_name': self.gauge_name,
                        'datetime': dt_str,
                        # 'date': dt.date(),
                        # 'time': dt.time(),
                        'stage': float(stage_str)
                    })
                # Sorting here will make the id for the entry non-sequential on the database.
                # data = sorted(combined_data, key=lambda k: (k['date'], k['time']), reverse=True)

                # Sorting here will make the id for the entry sequential on the database.
                combined_data = sorted(combined_data, key=lambda k: (k['datetime']))
                self.update_database(combined_data)
                return True, f'Successfully fetched river data.'
            return False, f'Failed to fetch river data.'

        except requests.exceptions.RequestException as e:
            return False, f'Error fetching river data: {e}'

    def update_database(self, data):
        for entry in data:
           self.model.objects.update_or_create(
                datetime=entry['datetime'],
                # date=entry['date'],
                # time=entry['time'],
                defaults={
                    'gauge_name': entry['gauge_name'],
                    'stage': entry['stage'],
                }
            )

class FetchGraniteFallsData(BaseFetchRiverData):
    gauge_name = 'Granite Falls'
    url = 'https://www.nwrfc.noaa.gov/xml/xml.cgi?id=GFLW1&pe=HG&dtype=b&numdays=10'
    model = GraniteFallsGauge


class FetchJordanRoadData(BaseFetchRiverData):
    gauge_name = 'Jordan Road'
    url = 'https://www.nwrfc.noaa.gov/xml/xml.cgi?id=SSFW1&pe=HG&dtype=b&numdays=10'
    model = JordanRoadGauge


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetches = [FetchGraniteFallsData(), FetchJordanRoadData()]
        combined_data = CombineCommand()
        a = datetime.now()
        for fetch in fetches:
            success, message = fetch.fetch_data()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))
        combined_data.handle()
        b = datetime.now()
        delta = b - a
        print(delta)
