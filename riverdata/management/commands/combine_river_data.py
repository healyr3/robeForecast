from django.core.management.base import BaseCommand

from riverdata.models import GraniteFallsGauge, JordanRoadGauge, CombinedGauges


class Command(BaseCommand):
    model = CombinedGauges

    def handle(self, *args, **options):
        try:
            # Delete tables entries for reset
            self.model.objects.all().delete()

            granite_falls_data = list(GraniteFallsGauge.objects.all().values('gauge_name', 'stage',
                                                                             'datetime'))
            jordan_road_data = list(JordanRoadGauge.objects.all().values('gauge_name', 'stage',
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
                    'gauge_B_name': None,
                    'gauge_B_stage': None,
                    'gauge_A_name': None,
                    'gauge_A_stage': None,
                }

                gd = next((g for g in granite_falls_data if g['datetime'] == dt), None)
                jd = next((j for j in jordan_road_data if j['datetime'] == dt), None)

                if gd:
                    entry['gauge_B_name'] = gd['gauge_name']
                    entry['gauge_B_stage'] = gd['stage']
                if jd:
                    entry['gauge_A_name'] = jd['gauge_name']
                    entry['gauge_A_stage'] = jd['stage']

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
                defaults={
                    'gauge_B_name': entry['gauge_B_name'],
                    'gauge_B_stage': entry['gauge_B_stage'],
                    'gauge_A_name': entry['gauge_A_name'],
                    'gauge_A_stage': entry['gauge_A_stage'],
                }
            )
