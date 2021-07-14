from django.contrib import admin
from django.urls import path, include
from doersclients import views

urlpatterns = [
    path('',  views.doersclients_list, name='doersclients_list'),
    path('doersclients/<int:pk>/',  views.doersclients_detail, name='doersclients_detail'),
]
