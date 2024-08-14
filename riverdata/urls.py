from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from . import views

# router = routers.DefaultRouter()
# router.register('riverdata', RiverDataViewSet)
urlpatterns = [
    path('riverdata/', views.RiverDataList.as_view(), name='river-data'),
]
