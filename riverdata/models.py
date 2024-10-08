from django.db import models


class BaseRiverData(models.Model):
    gauge_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
    stage = models.FloatField()

    class Meta:
        # unique_together = ('datetime', 'gauge_name')
        abstract = True

    def __str__(self):
        return str(vars(self))


class GraniteFallsGauge(BaseRiverData):
    pass


class JordanRoadGauge(BaseRiverData):
    pass


class CombinedGauges(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    gauge_1_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_1_stage = models.FloatField(null=True, blank=True)
    gauge_2_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_2_stage = models.FloatField(null=True, blank=True)


class CombinedPredictions(models.Model):
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
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

    def __str__(self):
        return str(vars(self))


class SilvertonWeatherPrediction(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    temp = models.FloatField()
    rain_3h = models.FloatField()
    snow_3h = models.FloatField()

    def __str__(self):
        return str(vars(self))


class AlpineMeadowsWeatherPrediction(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)
    temp = models.FloatField()
    rain_3h = models.FloatField()
    snow_3h = models.FloatField()

    def __str__(self):
        return str(vars(self))


class AlpineMeadowsGauge(models.Model):
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
    snow_water_equivalent = models.FloatField()
    snow_depth = models.FloatField()
    precipitation_accumulation = models.FloatField()
    air_temperature = models.FloatField()

    def __str__(self):
        return str(vars(self))


class GraniteFallsPrediction(models.Model):
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
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
    gauge_A_name = models.CharField(max_length=100, null=True, blank=True)
    gauge_A_stage = models.FloatField(null=True, blank=True)
    gauge_B_name = models.CharField(max_length=100)
    gauge_B_stage = models.FloatField()
    prediction_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(vars(self))


class GraniteFallsForecast(models.Model):
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
    gauge_name = models.CharField(max_length=100)
    stage = models.FloatField()
    prediction_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(vars(self))


class GraniteFallsPredictionLinear(models.Model):
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
    gauge_name = models.CharField(max_length=100)
    stage = models.FloatField()
    prediction_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(vars(self))


class GraniteFallsForecastLinear(models.Model):
    datetime = models.DateTimeField(null=True, blank=True, unique=True)
    gauge_name = models.CharField(max_length=100)
    stage = models.FloatField()
    prediction_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(vars(self))


class GraniteFallsPredictionArchive(models.Model):
    prediction_datetime = models.DateTimeField()
    gauge_name = models.CharField(max_length=100)
    stage = models.FloatField()
    forecast_datetime = models.DateTimeField()

    class Meta:
        unique_together = ('prediction_datetime', 'forecast_datetime')

    def __str__(self):
        return str(vars(self))


class GraniteFallsPredictionLinearArchive(models.Model):
    prediction_datetime = models.DateTimeField()
    gauge_name = models.CharField(max_length=100)
    stage = models.FloatField()
    forecast_datetime = models.DateTimeField()

    class Meta:
        unique_together = ('prediction_datetime', 'forecast_datetime')

    def __str__(self):
        return str(vars(self))


class AveragePrediction(models.Model):
    gauge_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(unique=True)
    average_predicted_stage = models.FloatField()
    observed_stage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(vars(self))


class AccuracyMetrics(models.Model):
    accuracy_period = models.IntegerField()
    mse = models.FloatField()
    mae = models.FloatField()
    r2 = models.FloatField()

    def __str__(self):
        return str(vars(self))


class AveragePredictionLinear(models.Model):
    gauge_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(unique=True)
    average_predicted_stage = models.FloatField()
    observed_stage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(vars(self))


class AccuracyMetricsLinear(models.Model):
    accuracy_period = models.IntegerField()
    mse = models.FloatField()
    mae = models.FloatField()
    r2 = models.FloatField()

    def __str__(self):
        return str(vars(self))
