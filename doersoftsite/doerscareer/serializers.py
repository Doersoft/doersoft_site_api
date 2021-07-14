from rest_framework import serializers
from .models import CareerCategory, Career, CareerForm

class CareerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCategory
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class CareerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerForm
        fields = '__all__'