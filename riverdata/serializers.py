from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (GraniteFallsForecast, AccuracyMetrics, AveragePrediction)


class GraniteFallsForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraniteFallsForecast
        fields = '__all__'


class AccuracyMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccuracyMetrics
        fields = '__all__'


class GraniteFallsForecastLinearSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraniteFallsForecast
        fields = '__all__'


class AveragePredictionLinearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AveragePrediction
        fields = '__all__'


class AccuracyMetricsLinearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccuracyMetrics
        fields = '__all__'
