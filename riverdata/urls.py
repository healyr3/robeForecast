from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from .views import RiverDataViewSet

# router = routers.DefaultRouter()
# router.register('riverdata', RiverDataViewSet)
urlpatterns = [
    path('riverdata/riverdata/', RiverDataViewSet.as_view(), name='riverdata'),
]
