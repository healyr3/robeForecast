from django.core.management.base import BaseCommand

from riverdata.models import GraniteFallsGauge, JordanRoadGauge, CombinedGauges


class Command(BaseCommand):
    model = CombinedGauges
    def handle(self, *args, **options):
        try:
            granite_falls_data = list(GraniteFallsGauge.objects.all().values('date', 'time', 'gauge_name', 'stage',
                                                                             'datetime'))
            jordan_road_data = list(JordanRoadGauge.objects.all().values('date', 'time', 'gauge_name', 'stage',
                                                                         'datetime'))

            all_keys = set()
            for data in [granite_falls_data, jordan_road_data]:
                for entry in data:
                    if entry['datetime'] is not None:
                        all_keys.add((entry['datetime']))

            combined_data = []
            for dt in sorted(all_keys):
                entry = {
                    'datetime': dt,
                    'date': None,
                    'time': None,
                    'gauge_1_name': None,
                    'gauge_1_stage': None,
                    'gauge_2_name': None,
                    'gauge_2_stage': None,
                }

                gd = next((g for g in granite_falls_data if g['datetime'] == dt), None)
                jd = next((j for j in jordan_road_data if j['datetime'] == dt), None)

                if gd:
                    entry['date'] = gd['date']
                    entry['time'] = gd['time']
                    entry['gauge_1_name'] = gd['gauge_name']
                    entry['gauge_1_stage'] = gd['stage']
                if jd:
                    entry['gauge_2_name'] = jd['gauge_name']
                    entry['gauge_2_stage'] = jd['stage']

                if gd and jd:
                    combined_data.append(entry)

            combined_data = sorted(combined_data, key=lambda k: (k['datetime']))

            self.update_database(combined_data)
            self.stdout.write(self.style.SUCCESS('Successfully combined river data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to combine river data: ' + str(e)))

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                datetime=entry['datetime'],
                date=entry['date'],
                time=entry['time'],
                defaults={
                    'gauge_1_name': entry['gauge_1_name'],
                    'gauge_1_stage': entry['gauge_1_stage'],
                    'gauge_2_name': entry['gauge_2_name'],
                    'gauge_2_stage': entry['gauge_2_stage'],
                }
            )

