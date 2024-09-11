from riverdata.management.commands.fetch_river_data import *
from riverdata.management.commands.fetch_weather_prediction import FetchSilvertonPrediction, FetchAlpineMeadowsPrediction
from riverdata.management.commands.fetch_alpine_meadows import FetchAlpineMeadowsGauge
class Command(BaseCommand):
    def handle(self, *args, **options):
        fetches = [FetchGraniteFallsData(), FetchJordanRoadData(), FetchSilvertonPrediction(),
                   FetchAlpineMeadowsPrediction(), FetchAlpineMeadowsGauge()]
        a = datetime.now()
        for fetch in fetches:
            success, message = fetch.fetch_data()
            if success:
                self.stdout.write(self.style.SUCCESS(message))
            else:
                self.stdout.write(self.style.ERROR(message))
        b = datetime.now()
        delta = b - a
        print(f'Time to fetch all river and weather data: {delta}')
