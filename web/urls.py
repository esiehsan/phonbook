from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('phonebook/all_persons/', views.all_persons), 
    path('', views.index), 
]