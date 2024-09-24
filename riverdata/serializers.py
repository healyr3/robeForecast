from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (GraniteFallsGauge, JordanRoadGauge, CombinedGauges, SilvertonWeatherPrediction,
                     AlpineMeadowsWeatherPrediction, AlpineMeadowsGauge, CombinedPredictions, GraniteFallsForecast,
                     AccuracyMetrics, AveragePrediction)


# class GraniteFallsGaugeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GraniteFallsGauge
#         fields = '__all__'
#
#
# class JordanRoadGaugeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = JordanRoadGauge
#         fields = '__all__'
#
#
# class CombinedGaugesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CombinedGauges
#         fields = '__all__'
#
#
# class CombinedPredictionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CombinedPredictions
#         fields = '__all__'
#
#
# class SilvertonWeatherPredictionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SilvertonWeatherPrediction
#         fields = '__all__'
#
#
# class AlpineMeadowsWeatherPredictionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SilvertonWeatherPrediction
#         fields = '__all__'
#
#
# class AlpineMeadowsGaugeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AlpineMeadowsGauge
#         fields = '__all__'
#
#
# class GraniteFallsPredictionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GraniteFallsGauge
#         fields = '__all__'


class GraniteFallsForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraniteFallsForecast
        fields = '__all__'


# class AveragePredictionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AveragePrediction
#         fields = '__all__'


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
