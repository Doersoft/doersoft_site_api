from django.contrib import admin
from django.urls import path, include
from doerscontact import views

urlpatterns = [
    path('',  views.contact_list, name='contact_list'),
    path('<int:pk>/',  views.contact_detail, name='contact_detail'),
]
