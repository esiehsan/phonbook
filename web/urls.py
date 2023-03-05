from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.persons, name='persons'), 
    path('reg/', views.register, name='register'),
    path('<int:person_id>/', views.detail, name='detail' ),
]