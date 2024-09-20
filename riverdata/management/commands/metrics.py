from datetime import datetime

from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        a = datetime.now()
        call_command('average_predictions')
        self.stdout.write(self.style.SUCCESS('Successfully averaged prediction data'))
        call_command('merge_observed_predicted')
        self.stdout.write(self.style.SUCCESS('Successfully merged predicted and observed data'))
        call_command('accuracy_metrics')
        self.stdout.write(self.style.SUCCESS('Successfully computed accuracy metrics'))
        b = datetime.now()
        delta = b - a
        print(f'Time to compute metrics: {delta}')
