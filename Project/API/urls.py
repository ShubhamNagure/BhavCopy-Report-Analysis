from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .views import getAllStocks,searchStocks
from . import views

urlpatterns = [
    path('all/',getAllStocks ), 
    path('all/<str:name>/',searchStocks ), 
]

