import re
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.core.management.base import BaseCommand, CommandError
from riverdata.models import RiverData

# Fetch river data for Granite Falls
class Command(BaseCommand):
    # def fetch_granite_falls(request):
    def handle(self, *args, **options):
        url = 'https://www.nwrfc.noaa.gov/xml/xml.cgi?id=GFLW1&pe=HG&dtype=b&numdays=10'
        # url = 'https://www.nwrfc.noaa.gov/station/flowplot/textPlot.cgi?id=GFLW1&pe=HG'
        try:
            response = requests.get(url)
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
                    stage = float(stage_str)
                    combined_data.append({
                        'riverID': '01',
                        'riverName': 'Granite Falls',
                        'datetime': dt,
                        'stage': stage
                    })

                for entry in combined_data:
                    RiverData.objects.update_or_create(
                        datetime=entry['datetime'],
                        defaults={
                            'stage': entry['stage'],
                            'riverID': entry['riverID'],
                            'riverName': entry['riverName'],
                        }
                    )

                self.stdout.write(self.style.SUCCESS('Successfully fetched river data.'))
            else:
                self.stdout.write(self.style.ERROR('Failed to fetch river data.'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching river data: {e}'))