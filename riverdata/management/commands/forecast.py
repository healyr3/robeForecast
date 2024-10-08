from datetime import datetime

from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        a = datetime.now()
        call_command('granite_falls_prediction')
        self.stdout.write(self.style.SUCCESS('Successfully executed Granite Falls prediction'))
        call_command('granite_falls_forecast')
        self.stdout.write(self.style.SUCCESS('Successfully fetched Granite Falls forecast'))
        call_command('granite_falls_prediction_linear')
        self.stdout.write(self.style.SUCCESS('Successfully executed Granite Falls prediction linear'))
        call_command('granite_falls_forecast_linear')
        self.stdout.write(self.style.SUCCESS('Successfully fetched Granite Falls forecast linear'))
        b = datetime.now()
        delta = b - a
        print(f'Time to forecast all data: {delta}')
