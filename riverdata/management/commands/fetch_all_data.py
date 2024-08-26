from django.core.management.base import BaseCommand, CommandError

from riverdata.management.commands.fetch_alpine_meadows import FetchAlpineMeadowsGauge
from riverdata.management.commands.fetch_river_data import *
from riverdata.management.commands.fetch_silverton_prediction import FetchSilvertonPrediction

class Command(BaseCommand):
    def handle(self, *args, **options):
        fetches = [FetchGraniteFallsData(), FetchJordanRoadData(), FetchVerlotData(), FetchSilvertonPrediction(),
                   FetchAlpineMeadowsGauge()]
        a = datetime.now()
        for fetch in fetches:
            success, message = fetch.fetch_data()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))
        b = datetime.now()
        delta = b - a
        print(f'Time to fetch all data: {delta}')
