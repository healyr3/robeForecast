from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

# from .models import GraniteFallsForecastLinear
from .views import (GraniteForecastList, AccuracyMetricsList, GraniteForecastLinearList,
                    GraniteFallsForecast, GraniteFallsForecastViewSet, GraniteFallsForecastLinearViewSet,
                    AccuracyMetricsLinearList, )

# from .views import (GraniteFallsGaugeList, JordanRoadGaugeList, CombindedGaugeList,
#                     SilvertonWeatherPredictionList, AlpineMeadowsGaugeList, jordan_chart, CombindedPredictionsList,
#                     granite_forecast_chart, GraniteForecastList, AccuracyMetricsList, AveragePredictionList)
urlpatterns = [
    # path('granitefalls/', GraniteFallsGaugeList.as_view(), name='granitefalls'),
    # path('jordanroad/', JordanRoadGaugeList.as_view(), name='jordanroad'),
    # path('combinedgauges/', CombindedGaugeList.as_view(), name='combinedgauges'),
    # path('combinedpredictions/', CombindedPredictionsList.as_view(), name='combinedpredictions'),
    # path('silvertonprediction/', SilvertonWeatherPredictionList.as_view(), name='silvertonprediction'),
    # path('alpinemeadowsprediction/', SilvertonWeatherPredictionList.as_view(), name='alpinemeadowsprediction'),
    # path('alpinemeadows/', AlpineMeadowsGaugeList.as_view(), name='alpinemeadows'),
    # path('jordanchart/', jordan_chart, name='jordanchart'),
    # path('granitefallsprediction/', GraniteFallsGaugeList.as_view(), name='granitefallsprediction'),
    path('granitefallsforecastchart/', GraniteFallsForecastViewSet.as_view({'get': 'granite_forecast_chart'}), name='granitefallsforecastchart'),
    path('granitefallsforecasttable/', GraniteForecastList.as_view(), name='granitefallsforecasttable'),
    path('accuracymetrics/', AccuracyMetricsList.as_view(), name='accuracymetrics'),
    # path('averageprediction/', AveragePredictionList.as_view(), name='averageprediction'),
    path('granitefallsforecastlinearchart/', GraniteFallsForecastLinearViewSet.as_view(
        {'get': 'granite_forecast_linear_chart'}),
         name='granitefallsforecastlinearchart'),
    path('granitefallsforecastlineartable/', GraniteForecastLinearList.as_view(),
         name='granitefallsforecastlineartable'),
    path('accuracymetricslinear/', AccuracyMetricsLinearList.as_view(), name='accuracymetricslinear'),

]
