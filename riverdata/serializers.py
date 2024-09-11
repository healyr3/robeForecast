from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import (GraniteFallsGauge, JordanRoadGauge, VerlotGauge, CombinedGauges, SilvertonWeatherPrediction,
                     AlpineMeadowsWeatherPrediction, AlpineMeadowsGauge, CombinedPredictions, GraniteFallsForecast)


class GraniteFallsGaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraniteFallsGauge
        fields = '__all__'

class JordanRoadGaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JordanRoadGauge
        fields = '__all__'

class VerlotGaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerlotGauge
        fields = '__all__'

class CombinedGaugesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombinedGauges
        fields = '__all__'

class CombinedPredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CombinedPredictions
        fields = '__all__'

class SilvertonWeatherPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilvertonWeatherPrediction
        fields = '__all__'

class AlpineMeadowsWeatherPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SilvertonWeatherPrediction
        fields = '__all__'

class AlpineMeadowsGaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlpineMeadowsGauge
        fields = '__all__'

class GraniteFallsPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraniteFallsGauge
        fields = '__all__'

class GraniteFallsForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraniteFallsForecast
        fields = '__all__'
