from datetime import datetime, timezone

from django.core.management.base import BaseCommand

from riverdata.models import (SilvertonWeatherPrediction, AlpineMeadowsWeatherPrediction, AlpineMeadowsGauge,
                              JordanRoadGauge, CombinedPredictions)

class Command(BaseCommand):
    model = CombinedPredictions

    def handle(self, *args, **options):
        try:
            # Delete tables entries for reset
            self.model.objects.all().delete()

            current_dt = datetime.now(timezone.utc)

            silverton_prediction = list(SilvertonWeatherPrediction.objects.filter(datetime__gt=current_dt).values(
                'datetime', 'temp', 'rain_3h', 'snow_3h'))

            alpine_meadows_prediction = list(AlpineMeadowsWeatherPrediction.objects.filter(datetime__gt=current_dt)
                                             .values('datetime', 'temp', 'rain_3h', 'snow_3h'))

            jordan_road_data = list(JordanRoadGauge.objects.filter(datetime__gt=current_dt).values('datetime',
                                                                                                   'gauge_name',
                                                                                                   'stage'))

            alpine_meadows_data = AlpineMeadowsGauge.objects.latest('snow_water_equivalent',
                                                                    'snow_depth',
                                                                    'precipitation_accumulation',
                                                                    'air_temperature')

            all_keys = set()
            for data in [silverton_prediction, alpine_meadows_prediction, jordan_road_data]:
                for entry in data:
                    all_keys.add((entry['datetime']))

            combined_data = []
            for dt in sorted(all_keys):
                entry = {
                    'datetime': dt,
                    'sp_temp': None,
                    'sp_rain_3h': None,
                    'sp_snow_3h': None,
                    'ap_temp': None,
                    'ap_rain_3h': None,
                    'ap_snow_3h': None,
                    'gauge_name': None,
                    'gauge_stage': None,
                    'am_snow_water_equivalent': None,
                    'am_snow_depth': None,
                    'am_precipitation_accumulation': None,
                    'am_air_temperature': None,
                }

                sp = next((s for s in silverton_prediction if s['datetime'] == dt), None)
                ap = next((a for a in alpine_meadows_prediction if a['datetime'] == dt), None)
                jd = next((j for j in jordan_road_data if j['datetime'] == dt), None)

                if sp:
                    entry['sp_temp'] = sp['temp']
                    entry['sp_rain_3h'] = sp['rain_3h']
                    entry['sp_snow_3h'] = sp['snow_3h']
                if ap:
                    entry['ap_temp'] = ap['temp']
                    entry['ap_rain_3h'] = ap['rain_3h']
                    entry['ap_snow_3h'] = ap['snow_3h']
                if jd:
                    entry['gauge_name'] = jd['gauge_name']
                    entry['gauge_stage'] = jd['stage']
                if alpine_meadows_data:
                    entry['am_snow_water_equivalent'] = alpine_meadows_data.snow_water_equivalent
                    entry['am_snow_depth'] = alpine_meadows_data.snow_depth
                    entry['am_precipitation_accumulation'] = alpine_meadows_data.precipitation_accumulation
                    entry['am_air_temperature'] = alpine_meadows_data.air_temperature

                if sp and ap and jd:
                    combined_data.append(entry)

            combined_data = sorted(combined_data, key=lambda k: (k['datetime']))

            self.update_database(combined_data)

            self.stdout.write(self.style.SUCCESS('Successfully combined prediction data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to combine prediction data: ' + str(e)))

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                datetime=entry['datetime'],
                defaults={
                    'sp_temp': entry['sp_temp'],
                    'sp_rain_3h': entry['sp_rain_3h'],
                    'sp_snow_3h': entry['sp_snow_3h'],
                    'ap_temp': entry['ap_temp'],
                    'ap_rain_3h': entry['ap_rain_3h'],
                    'ap_snow_3h': entry['ap_snow_3h'],
                    'gauge_name': entry['gauge_name'],
                    'gauge_stage': entry['gauge_stage'],
                    'am_snow_water_equivalent': entry['am_snow_water_equivalent'],
                    'am_snow_depth': entry['am_snow_depth'],
                    'am_precipitation_accumulation': entry['am_precipitation_accumulation'],
                    'am_air_temperature': entry['am_air_temperature'],
                }
            )

