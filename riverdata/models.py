from django.db import models


class BaseRiverData(models.Model):
    gauge_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    stage = models.FloatField()

    class Meta:
        unique_together = ('date', 'time')
        abstract = True

    def __str__(self):
        return f'{self.gauge_name} - {self.date}  - {self.time} - {self.stage}'


class GraniteFallsGauge(BaseRiverData):
    pass


class JordanRoadGauge(BaseRiverData):
    pass


class CombinedGauges(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    gauge_1_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_1_stage = models.FloatField(null=True, blank=True)
    gauge_2_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_2_stage = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return (f'{str(self.date)} - {self.time} - self.{self.gauge_1_name} - {self.gauge_1_stage} - '
                f'{self.gauge_2_name} - {self.gauge_2_stage}')


class CombinedPredictions(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    sp_temp = models.FloatField(null=True, blank=True)
    sp_rain_3h = models.FloatField(null=True, blank=True)
    sp_snow_3h = models.FloatField(null=True, blank=True)
    ap_temp = models.FloatField(null=True, blank=True)
    ap_rain_3h = models.FloatField(null=True, blank=True)
    ap_snow_3h = models.FloatField(null=True, blank=True)
    gauge_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_stage = models.FloatField(null=True, blank=True)
    am_snow_water_equivalent = models.FloatField(null=True, blank=True)
    am_snow_depth = models.FloatField(null=True, blank=True)
    am_precipitation_accumulation = models.FloatField(null=True, blank=True)
    am_air_temperature = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return (
            f'{str(self.date)} - {self.time} - self.{self.sp_temp} - self.{self.sp_rain_3h} - self.{self.sp_snow_3h} - self.{self.ap_temp} - self.{self.ap_rain_3h} - self.{self.ap_snow_3h} - self.{self.gauge_name} - self.{self.gauge_stage})')


class SilvertonWeatherPrediction(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    temp = models.FloatField()
    rain_3h = models.FloatField()
    snow_3h = models.FloatField()

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return f'{self.date} - {self.time} - {self.temp} - {self.rain_3h} - {self.snow_3h}'


class AlpineMeadowsWeatherPrediction(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    temp = models.FloatField()
    rain_3h = models.FloatField()
    snow_3h = models.FloatField()

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return f'{self.date} - {self.time} - {self.temp} - {self.rain_3h} - {self.snow_3h}'


class AlpineMeadowsGauge(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
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


class GraniteFallsPrediction(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    sp_temp = models.FloatField(null=True, blank=True)
    sp_rain_3h = models.FloatField(null=True, blank=True)
    sp_snow_3h = models.FloatField(null=True, blank=True)
    ap_temp = models.FloatField(null=True, blank=True)
    ap_rain_3h = models.FloatField(null=True, blank=True)
    ap_snow_3h = models.FloatField(null=True, blank=True)
    am_snow_water_equivalent = models.FloatField(null=True, blank=True)
    am_snow_depth = models.FloatField(null=True, blank=True)
    am_precipitation_accumulation = models.FloatField(null=True, blank=True)
    am_air_temperature = models.FloatField(null=True, blank=True)
    gauge2_name = models.CharField(max_length=100, null=True, blank=True)
    gauge2_stage = models.FloatField(null=True, blank=True)
    gauge1_name = models.CharField(max_length=100)
    gauge1_stage = models.FloatField()
    prediction_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return (
            f'{self.date}  - {self.time} - self.{self.sp_temp} - self.{self.sp_rain_3h} - self.{self.sp_snow_3h} - '
            f'self.{self.ap_temp} - self.{self.ap_rain_3h} - self.{self.ap_snow_3h} - self.{self.gauge2_name} - '
            f'self.{self.gauge2_stage} - {self.gauge1_name} - {self.gauge1_stage} - {self.prediction_datetime}')


class GraniteFallsForecast(BaseRiverData):
    prediction_datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('date', 'time')

    def __str__(self):
        return f'{self.gauge_name} - {self.date}  - {self.time} - {self.stage} - {self.prediction_datetime}'

    # def __init__(self):
    #     super().__init__()
    #     self.prediction_datetime = models.DateTimeField()
