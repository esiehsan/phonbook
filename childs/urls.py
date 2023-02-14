from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('employees/', views.employees), 
    path('childs/<str:nCode>/', views.childs),
]