from django.contrib import admin
from django.urls import path, include
from doerscareer import views

urlpatterns = [
    path('CareerCategory/',  views.CareerCategory_list, name='careercategory_list'),
    path('<int:pk>/',  views.CareerCategory_detail, name='careercategory_detail'),
    path('',  views.Career_list, name='career_list'),
    path('CareerCategory/<int:pk>/',  views.Career_detail, name='careerc_detail'),
    path('CareerForm/',  views.CareerForm_list, name='careerform_list'),
    path('CareerForm/<int:pk>/',  views.CareerForm_detail, name='careerform_detail'),
]
