import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django.utils import timezone

from rest_framework import viewsets, status, authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from .models import GraniteFallsGauge, JordanRoadGauge, CombinedGauges, SilvertonWeatherPrediction, \
    AlpineMeadowsGauge, AlpineMeadowsWeatherPrediction, CombinedPredictions, GraniteFallsForecast, AccuracyMetrics, \
    AveragePrediction, GraniteFallsForecastLinear, AccuracyMetricsLinear
from .serializers import GraniteFallsForecastSerializer, AccuracyMetricsSerializer, \
    GraniteFallsForecastLinearSerializer, AccuracyMetricsLinearSerializer

# from .serializers import GraniteFallsGaugeSerializer, JordanRoadGaugeSerializer, \
#     CombinedGaugesSerializer, SilvertonWeatherPredictionSerializer, AlpineMeadowsGaugeSerializer, \
#     AlpineMeadowsWeatherPredictionSerializer, CombinedPredictionsSerializer, GraniteFallsPredictionSerializer, \
#     GraniteFallsForecastSerializer, AccuracyMetricsSerializer, AveragePredictionSerializer

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from datetime import datetime, timezone
from dateutil import tz


# class GraniteFallsGaugeList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         river_data = GraniteFallsGauge.objects.all()
#         serializer = GraniteFallsGaugeSerializer(river_data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class JordanRoadGaugeList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         river_data = JordanRoadGauge.objects.all()
#         serializer = JordanRoadGaugeSerializer(river_data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class CombindedGaugeList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         combined_gauges = CombinedGauges.objects.all().order_by('-datetime')
#         serializer = CombinedGaugesSerializer(combined_gauges, many=True)
#
#         data = serializer.data
#
#         for entry in data:
#             utc_dt = datetime.strptime(entry['datetime'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
#             local_datetime = utc_dt.astimezone(tz.tzlocal())
#             # print(utc_datetime, local_datetime)
#
#             entry['date'] = local_datetime.strftime('%m-%d-%y')
#             entry['time'] = local_datetime.strftime('%I:%M %p')
#
#         return Response(data, status=status.HTTP_200_OK)
#
#
# class CombindedPredictionsList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         combined_predictions = CombinedPredictions.objects.all().order_by('-datetime')
#         serializer = CombinedPredictionsSerializer(combined_predictions, many=True)
#
#         data = serializer.data
#
#         for entry in data:
#             utc_dt = datetime.strptime(entry['datetime'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
#             local_datetime = utc_dt.astimezone(tz.tzlocal())
#             # print(utc_datetime, local_datetime)
#
#             entry['date'] = local_datetime.strftime('%m-%d-%y')
#             entry['time'] = local_datetime.strftime('%I:%M %p')
#
#         return Response(data, status=status.HTTP_200_OK)
#
#
# class SilvertonWeatherPredictionList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         silverton_weather = SilvertonWeatherPrediction.objects.all().order_by('-datetime')
#         serializer = SilvertonWeatherPredictionSerializer(silverton_weather, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class AlpineMeadowsWeatherPredictionList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         alpine_meadows_weather = AlpineMeadowsWeatherPrediction.objects.all().order_by('-datetime')
#         serializer = AlpineMeadowsWeatherPredictionSerializer(alpine_meadows_weather, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class AlpineMeadowsGaugeList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         alpine_meadows = AlpineMeadowsGauge.objects.all().order_by('-datetime')
#         serializer = AlpineMeadowsGaugeSerializer(alpine_meadows, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# def jordan_chart(request):
#     river_data = JordanRoadGauge.objects.all()
#
#     df = pd.DataFrame(list(river_data.values('date', 'time', 'stage')))
#     df['datetime_utc'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str)).dt.tz_localize('UTC')
#     df['datetime_local'] = df['datetime_utc'].dt.tz_convert(tz.tzlocal())
#     df.sort_values(by='datetime_local', inplace=True)
#
#     print(df.datetime_local)
#
#     df['type'] = 'Observed'
#     now = datetime.now(tz=tz.tzlocal()).strftime('%Y-%m-%d %H:%M:%S')
#     df.loc[df['datetime_local'] > now, 'type'] = 'Forecast'
#
#     print(now)
#
#     fig = px.line(
#         df,
#         x='datetime_local',
#         y='stage',
#         color='type',
#         title='Jordan River Stage'
#     )
#
#     # chart_html = fig.to_html(full_html=False)
#     #
#     # return JsonResponse({'chart': chart_html}
#     chart_dict = fig.to_dict()
#
#     def convert_np_to_list(obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         elif isinstance(obj, dict):
#             return {k: convert_np_to_list(v) for k, v in obj.items()}
#         elif isinstance(obj, list):
#             return [convert_np_to_list(elem) for elem in obj]
#         else:
#             return obj
#
#     chart_json = convert_np_to_list(chart_dict)
#
#     return JsonResponse({'chart': chart_json})
#
#
# class GraniteFallsPrediction(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         river_data = GraniteFallsPrediction.objects.all()
#         serializer = GraniteFallsPredictionSerializer(river_data, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class GraniteFallsForecastViewSet(viewsets.ModelViewSet):
    queryset = GraniteFallsForecast.objects.all()
    permission_classes = [AllowAny]
    @action(detail=False, methods=['GET'])
    def granite_forecast_chart(self, request):
        river_data = GraniteFallsForecast.objects.all()

        df = pd.DataFrame(list(river_data.values('datetime', 'stage')))
        df['datetime_local'] = df['datetime'].dt.tz_convert(tz.tzlocal())
        df.sort_values(by='datetime_local', inplace=True)

        df['Category'] = 'Observed'
        now = datetime.now(tz=tz.tzlocal()).strftime('%Y-%m-%d %H:%M:%S')
        df.loc[df['datetime_local'] > now, 'Category'] = 'Forecast'

        fig = px.line(
            df,
            x='datetime_local',
            y='stage',
            color='Category',
            title='Granite Falls \'Robe\' Stage - Random Forest Forecast',
            labels={'datetime_local': '', 'stage': 'Stage [ft]', 'Category': ''},
        )

        fig.add_trace(
            go.Scatter(
                x=[df['datetime_local'].min(), df['datetime_local'].max()],  # x-coordinates
                y=[6, 6],  # y-coordinates for the line
                line=go.scatter.Line(color='Purple', width=2, dash='dash'),
                name='Mortal Limit'
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[df['datetime_local'].min(), df['datetime_local'].max()],  # x-coordinates
                y=[5.5, 5.5],  # y-coordinates for the line
                line=go.scatter.Line(color='Green', width=2, dash='dash'),
                name='Getting Good'
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[df['datetime_local'].min(), df['datetime_local'].max()],  # x-coordinates
                y=[5, 5],  # y-coordinates for the line
                line=go.scatter.Line(color='Orange', width=2, dash='dash'),
                name='A Bit Low'
            )
        )

        fig.update_layout(
            legend=dict(
                x=0.009,  # X position of the legend (0 is left, 1 is right)
                y=0.97,  # Y position of the legend (0 is bottom, 1 is top)
                xanchor="left",  # Anchor point of the legend (left, center, right)
                yanchor="top",  # Anchor point of the legend (top, middle, bottom)
                bgcolor='rgba(255, 255, 255, 0.85)'  # Transparent background for the legend
            )
        )

        # fig.update_layout(config=dict(responsive=True))

        # chart_html = fig.to_html(full_html=False)
        #
        # return JsonResponse({'chart': chart_html}
        chart_dict = fig.to_dict()

        def convert_np_to_list(obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {k: convert_np_to_list(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_np_to_list(elem) for elem in obj]
            else:
                return obj

        chart_json = convert_np_to_list(chart_dict)

        return JsonResponse({'chart': chart_json})


class GraniteFallsForecastLinearViewSet(viewsets.ModelViewSet):
    queryset = GraniteFallsForecast.objects.all()
    permission_classes = [AllowAny]
    @action(detail=False, methods=['GET'])
    def granite_forecast_linear_chart(self, request):
        river_data = GraniteFallsForecastLinear.objects.all()

        df = pd.DataFrame(list(river_data.values('datetime', 'stage')))
        df['datetime_local'] = df['datetime'].dt.tz_convert(tz.tzlocal())
        df.sort_values(by='datetime_local', inplace=True)

        df['Category'] = 'Observed'
        now = datetime.now(tz=tz.tzlocal()).strftime('%Y-%m-%d %H:%M:%S')
        df.loc[df['datetime_local'] > now, 'Category'] = 'Forecast'

        fig = px.line(
            df,
            x='datetime_local',
            y='stage',
            color='Category',
            title='Granite Falls \'Robe\' Stage - Linear Forecast',
            labels={'datetime_local': '', 'stage': 'Stage [ft]', 'Category': ''},
        )

        fig.add_trace(
            go.Scatter(
                x=[df['datetime_local'].min(), df['datetime_local'].max()],  # x-coordinates
                y=[6, 6],  # y-coordinates for the line
                line=go.scatter.Line(color='Purple', width=2, dash='dash'),
                name='Mortal Limit'
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[df['datetime_local'].min(), df['datetime_local'].max()],  # x-coordinates
                y=[5.5, 5.5],  # y-coordinates for the line
                line=go.scatter.Line(color='Green', width=2, dash='dash'),
                name='Getting Good'
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[df['datetime_local'].min(), df['datetime_local'].max()],  # x-coordinates
                y=[5, 5],  # y-coordinates for the line
                line=go.scatter.Line(color='Orange', width=2, dash='dash'),
                name='A Bit Low'
            )
        )

        fig.update_layout(
            legend=dict(
                x=0.009,  # X position of the legend (0 is left, 1 is right)
                y=0.97,  # Y position of the legend (0 is bottom, 1 is top)
                xanchor="left",  # Anchor point of the legend (left, center, right)
                yanchor="top",  # Anchor point of the legend (top, middle, bottom)
                bgcolor='rgba(255, 255, 255, 0.85)'  # Transparent background for the legend
            )
        )

        # chart_html = fig.to_html(full_html=False)
        #
        # return JsonResponse({'chart': chart_html}
        chart_dict = fig.to_dict()

        def convert_np_to_list(obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {k: convert_np_to_list(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_np_to_list(elem) for elem in obj]
            else:
                return obj

        chart_json = convert_np_to_list(chart_dict)

        return JsonResponse({'chart': chart_json})


class GraniteForecastList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        river_data = GraniteFallsForecast.objects.all()
        serializer = GraniteFallsForecastSerializer(river_data, many=True)
        now_utc = datetime.now(timezone.utc)
        filtered_data = []

        for entry in serializer.data:
            utc_dt = datetime.strptime(entry['datetime'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
            if utc_dt > now_utc:
                filtered_data.append(entry)

        for entry in filtered_data:
            utc_dt = datetime.strptime(entry['datetime'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
            local_datetime = utc_dt.astimezone(tz.tzlocal())

            entry['date'] = local_datetime.strftime('%a, %b %d')
            entry['time'] = local_datetime.strftime('%I:%M %p')

        return Response(filtered_data, status=status.HTTP_200_OK)


class GraniteForecastLinearList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        river_data = GraniteFallsForecastLinear.objects.all()
        serializer = GraniteFallsForecastLinearSerializer(river_data, many=True)
        now_utc = datetime.now(timezone.utc)
        filtered_data = []

        for entry in serializer.data:
            utc_dt = datetime.strptime(entry['datetime'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
            if utc_dt > now_utc:
                filtered_data.append(entry)

        for entry in filtered_data:
            utc_dt = datetime.strptime(entry['datetime'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
            local_datetime = utc_dt.astimezone(tz.tzlocal())

            entry['date'] = local_datetime.strftime('%a, %b %d')
            entry['time'] = local_datetime.strftime('%I:%M %p')

        return Response(filtered_data, status=status.HTTP_200_OK)


# class AveragePredictionList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         average_prediction = AveragePrediction.objects.all()
#         serializer = AveragePredictionSerializer(average_prediction, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class AccuracyMetricsList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        accuracy_metrics = AccuracyMetrics.objects.all()
        serializer = AccuracyMetricsSerializer(accuracy_metrics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccuracyMetricsLinearList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        accuracy_metrics = AccuracyMetricsLinear.objects.all()
        serializer = AccuracyMetricsLinearSerializer(accuracy_metrics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
