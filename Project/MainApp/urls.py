from django.contrib import admin

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', upload, name='upload'),
]