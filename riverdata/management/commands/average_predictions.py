from django.core.management import BaseCommand
from django.db.models import Avg

from riverdata.models import GraniteFallsPredictionArchive, AveragePrediction


class Command(BaseCommand):
    model = AveragePrediction
    def handle(self, *args, **options):
        try:
            pred_avg = GraniteFallsPredictionArchive.objects.values('forecast_datetime').annotate(average_value=Avg(
                'stage'))

            self.update_database(pred_avg)

            self.stdout.write(self.style.SUCCESS('Successfully averaged predictions.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Failed to average predictions: ' + str(e)))

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                datetime=entry['forecast_datetime'],
                defaults={
                    'gauge_name': 'Granite Falls',
                    'average_predicted_stage': entry['average_value'],
                }
            )

