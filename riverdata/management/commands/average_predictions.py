from django.core.management import BaseCommand
from django.db.models import Avg

from riverdata.models import GraniteFallsPredictionArchive, AveragePrediction, AveragePredictionLinear, \
    GraniteFallsPredictionLinearArchive


class BaseAveragePrediction:
    archive = None
    def average_prediction(self):
        try:
            pred_avg = self.archive.objects.values('forecast_datetime').annotate(average_value=Avg(
                'stage'))

            self.update_database(pred_avg)

            return True, f'Successfully averaged predictions.'

        except Exception as e:
            return False, f'Failed to average predictions: '

    def update_database(self, data):
        for entry in data:
            self.model.objects.update_or_create(
                datetime=entry['forecast_datetime'],
                defaults={
                    'gauge_name': 'Granite Falls',
                    'average_predicted_stage': entry['average_value'],
                }
            )


class AveragePredictionRF(BaseAveragePrediction):
    model = AveragePrediction
    archive = GraniteFallsPredictionArchive


class AveragePredictionLinear(BaseAveragePrediction):
    model = AveragePredictionLinear
    archive = GraniteFallsPredictionLinearArchive


class Command(BaseCommand):
    def handle(self, *args, **options):
        tasks = [AveragePredictionRF(), AveragePredictionLinear()]
        for task in tasks:
            success, message = task.average_prediction()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))

