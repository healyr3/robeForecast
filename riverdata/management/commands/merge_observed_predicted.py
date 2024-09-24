from django.core.management.base import BaseCommand

from riverdata.models import AveragePrediction, GraniteFallsGauge, AveragePredictionLinear


class BaseMergeCommand:
    # model = AveragePrediction

    def merge_observed_predicted(self):

        try:
            average_prediction_data = list(self.model.objects.all().values('datetime',
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

            return True, f'Successfully computed accuracy metrics.'

        except Exception as e:
            return False, f'Failed to compute accuracy metrics: '

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

class AveragePredictionRF(BaseMergeCommand):
    model = AveragePrediction


class AveragePredictionLinear(BaseMergeCommand):
    model = AveragePredictionLinear


class Command(BaseCommand):
    def handle(self, *args, **options):
        tasks = [AveragePredictionRF(), AveragePredictionLinear()]
        for task in tasks:
            success, message = task.merge_observed_predicted()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))
