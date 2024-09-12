from datetime import datetime

from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        a = datetime.now()
        call_command('fetch_all_data')
        self.stdout.write(self.style.SUCCESS('Successfully fetched all data'))
        call_command('combine_predictions')
        self.stdout.write(self.style.SUCCESS('Successfully combined predictions'))
        b = datetime.now()
        delta = b - a
        print(f'Time to fetch all data: {delta}')
