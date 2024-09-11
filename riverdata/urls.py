from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from .views import (GraniteFallsGaugeList, JordanRoadGaugeList, VerlotGaugeList, CombindedGaugeList,
                    SilvertonWeatherPredictionList, AlpineMeadowsGaugeList, jordan_chart, CombindedPredictionsList,
                    granite_forecast_chart, GraniteForecastList)

urlpatterns = [
    path('granitefalls/', GraniteFallsGaugeList.as_view(), name='granitefalls'),
    path('jordanroad/', JordanRoadGaugeList.as_view(), name='jordanroad'),
    path('verlot/', VerlotGaugeList.as_view(), name='verlot'),
    path('combinedgauges/', CombindedGaugeList.as_view(), name='combinedgauges'),
    path('combinedpredictions/', CombindedPredictionsList.as_view(), name='combinedpredictions'),
    path('silvertonprediction/', SilvertonWeatherPredictionList.as_view(), name='silvertonprediction'),
    path('alpinemeadowsprediction/', SilvertonWeatherPredictionList.as_view(), name='alpinemeadowsprediction'),
    path('alpinemeadows/', AlpineMeadowsGaugeList.as_view(), name='alpinemeadows'),
    path('jordanchart/', jordan_chart, name='jordanchart'),
    path('granitefallsprediction/', GraniteFallsGaugeList.as_view(), name='granitefallsprediction'),
    path('granitefallsforecastchart/', granite_forecast_chart, name='granitefallsforecastchart'),
    path('granitefallsforecasttable/', GraniteForecastList.as_view(), name='granitefallsforecasttable'),

]
