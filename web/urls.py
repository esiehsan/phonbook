from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('all_persons/', views.all_persons), 
]