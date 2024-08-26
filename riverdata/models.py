from django.db import models

class BaseRiverData(models.Model):
    river_id = models.IntegerField()
    gauge_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    stage = models.FloatField()

    class Meta:
        unique_together = ('river_id', 'date', 'time')
        abstract = True

    def __str__(self):
        return f'{self.gauge_name} - {self.date}  - {self.time} - {self.stage}'

class GraniteFallsGauge(BaseRiverData):
    pass

class JordanRoadGauge(BaseRiverData):
    pass

class VerlotGauge(BaseRiverData):
    pass

class CombinedGauges(models.Model):
    date = models.DateField()
    time = models.TimeField()
    gauge_1_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_1_stage = models.FloatField(null=True, blank=True)
    gauge_2_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_2_stage = models.FloatField(null=True, blank=True)
    gauge_3_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_3_stage = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return (f'{str(self.date)} - {self.time} - self.{self.gauge_1_name} - {self.gauge_1_stage} - '
                f'{self.gauge_2_name} - {self.gauge_2_stage} - {self.gauge_3_name} - {self.gauge_3_stage}')

class SilvertonWeatherPrediction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    temp = models.FloatField()
    rain_3h = models.FloatField()

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return f'{self.date} - {self.time} - {self.temp} - {self.rain_3h}'

class AlpineMeadowsGauge(models.Model):
    date = models.DateField()
    time = models.TimeField()
    snow_water_equivalent = models.FloatField()
    snow_depth = models.FloatField()
    precipitation_accumulation = models.FloatField()
    air_temperature = models.FloatField()

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return (f'{self.date} - {self.time} - {self.snow_water_equivalent} - {self.snow_depth} - '
                f'{self.precipitation_accumulation} - {self.air_temperature}')
