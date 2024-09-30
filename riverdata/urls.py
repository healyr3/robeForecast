from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (GraniteForecastList, AccuracyMetricsList, GraniteForecastLinearList, GraniteFallsForecastViewSet,
                    GraniteFallsForecastLinearViewSet, AccuracyMetricsLinearList, )

urlpatterns = [
    path('granitefallsforecastchart/', GraniteFallsForecastViewSet.as_view({'get': 'granite_forecast_chart'}),
         name='granitefallsforecastchart'),
    path('granitefallsforecasttable/', GraniteForecastList.as_view(), name='granitefallsforecasttable'),
    path('accuracymetrics/', AccuracyMetricsList.as_view(), name='accuracymetrics'),
    path('granitefallsforecastlinearchart/', GraniteFallsForecastLinearViewSet.as_view(
        {'get': 'granite_forecast_linear_chart'}), name='granitefallsforecastlinearchart'),
    path('granitefallsforecastlineartable/', GraniteForecastLinearList.as_view(),
         name='granitefallsforecastlineartable'),
    path('accuracymetricslinear/', AccuracyMetricsLinearList.as_view(), name='accuracymetricslinear'),

]
