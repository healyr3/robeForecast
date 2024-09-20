from django.core.management.base import BaseCommand

from riverdata.models import AveragePrediction, GraniteFallsGauge


class Command(BaseCommand):
    model = AveragePrediction

    def handle(self, *args, **options):
        try:
            average_prediction_data = list(AveragePrediction.objects.all().values('datetime',
                                                                                  'average_predicted_stage'))

            observed_data = list(GraniteFallsGauge.objects.all().values('datetime', 'stage'))

            all_keys = set()
            for data in [average_prediction_data, observed_data]:
                for entry in data:
                    if entry['datetime'] is not None:
                        all_keys.add((entry['datetime']))

            combined_data = []
            for dt in sorted(all_keys):
                entry = {
                    'datetime': dt,
                    'avg_pred_stage': None,
                    'observed_stage': None,
                }

                aps = next((a for a in average_prediction_data if a['datetime'] == dt), None)
                os = next((o for o in observed_data if o['datetime'] == dt), None)

                if aps:
                    entry['avg_pred_stage'] = aps['average_predicted_stage']
                if os:
                    entry['observed_stage'] = os['stage']

                if aps and os:
                    combined_data.append(entry)

            combined_data = sorted(combined_data, key=lambda k: (k['datetime']))

            self.update_database(combined_data)

            self.stdout.write(self.style.SUCCESS('Successfully computed accuracy metrics.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to compute accuracy metrics: ' + str(e)))

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                datetime=entry['datetime'],
                defaults={
                    'gauge_name': 'Granite Falls',
                    'average_predicted_stage': entry['avg_pred_stage'],
                    'observed_stage': entry['observed_stage'],
                }
            )
