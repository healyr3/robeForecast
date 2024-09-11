from datetime import datetime

from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        a = datetime.now()
        call_command('fetch_all_data')
        self.stdout.write(self.style.SUCCESS('Successfully fetched all data'))
        call_command('combine_predictions')
        self.stdout.write(self.style.SUCCESS('Successfully combined predictions'))
        call_command('granite_falls_prediction')
        self.stdout.write(self.style.SUCCESS('Successfully fetched granite falls prediction'))
        call_command('granite_falls_forecast')
        self.stdout.write(self.style.SUCCESS('Successfully fetched granite falls forecast'))
        b = datetime.now()
        delta = b - a
        print(f'Time to fetch all data: {delta}')
