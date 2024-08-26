from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from .views import (GraniteFallsGaugeList, JordanRoadGaugeList, VerlotGaugeList, CombindedGaugeList,
                    SilvertonWeatherPredictionList, AlpineMeadowsGaugeList, jordan_chart)

urlpatterns = [
    path('granitefalls/', GraniteFallsGaugeList.as_view(), name='granitefalls'),
    path('jordanroad/', JordanRoadGaugeList.as_view(), name='jordanroad'),
    path('verlot/', VerlotGaugeList.as_view(), name='verlot'),
    path('combinedgauges/', CombindedGaugeList.as_view(), name='combinedgauges'),
    path('silvertonprediction/', SilvertonWeatherPredictionList.as_view(), name='silvertonprediction'),
    path('alpinemeadows/', AlpineMeadowsGaugeList.as_view(), name='alpinemeadows'),
    path('jordanchart/', jordan_chart, name='jordanchart'),
]
