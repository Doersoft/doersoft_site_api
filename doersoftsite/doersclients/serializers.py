from rest_framework import serializers
from .models import DoersClients, DoersProduct

class DoersClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoersClients
        # fields = '__all__'
        fields = ['id','client_name']

class DoersProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoersProduct
        fields = '__all__'