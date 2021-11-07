from django.contrib import admin

from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.redisDBandCache, name='index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('chart/', ChartView.as_view(), name="chart"),
    path('chart/', views.getFilterChart, name="chart"),
]