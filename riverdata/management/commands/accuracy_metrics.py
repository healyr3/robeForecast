from datetime import datetime, timezone, timedelta

from django.core.management.base import BaseCommand
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

from riverdata.models import AveragePrediction, AccuracyMetrics


class BaseComputeMetrics:
    model = AccuracyMetrics

    def compute_metrics(self):
        try:
            current_datetime = datetime.now(timezone.utc)
            time_offset = current_datetime - timedelta(days=self.time_period)

            average_prediction_data = list(AveragePrediction.objects.filter(datetime__gte=time_offset).values(
                'datetime',
                'average_predicted_stage',
                'observed_stage'))

            observed_data = []
            predicted_data = []
            accuracy_metrics = {}

            for entry in average_prediction_data:
                if entry['observed_stage']:
                    observed_data.append(entry['observed_stage'])
                    predicted_data.append(entry['average_predicted_stage'])

            mse = mean_squared_error(observed_data, predicted_data)
            mae = mean_absolute_error(observed_data, predicted_data)
            r2 = r2_score(observed_data, predicted_data)

            accuracy_metrics['accuracy_period'] = self.time_period
            accuracy_metrics['mse'] = round(mse, 5)
            accuracy_metrics['mae'] = round(mae, 5)
            accuracy_metrics['r2'] = round(r2, 5)

            self.update_database(accuracy_metrics)

            return True, f'Successfully computed accuracy metrics for {self.time_period} days.'

        except Exception as e:
            return False, f'Failed to compute accuracy metrics for {self.time_period} days: {e}'

    def update_database(self, data):
        self.model.objects.update_or_create(
            accuracy_period=data['accuracy_period'],
            defaults={
                'mse': data['mse'],
                'mae': data['mae'],
                'r2': data['r2'],
            }
        )

class ComputeWeekMetrics(BaseComputeMetrics):
    time_period = 7

class ComputeMonthMetrics(BaseComputeMetrics):
    time_period = 30

class ComputeQuarterMetrics(BaseComputeMetrics):
    time_period = 91

class Command(BaseCommand):
    def handle(self, *args, **options):
        computations = [ComputeWeekMetrics(), ComputeMonthMetrics(), ComputeQuarterMetrics()]
        for computation in computations:
            success, message = computation.compute_metrics()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))



