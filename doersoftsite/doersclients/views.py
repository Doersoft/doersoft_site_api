from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from doersclients.models import DoersClients, DoersProduct
from doersclients.serializers import DoersClientsSerializer, DoersProductSerializer
from rest_framework.response import Response

@csrf_exempt
def doersclients_list(request):
    """
    List all doersclients list, or create a new snippet.
    """
    if request.method == 'GET':
        dc = DoersClients.objects.all()
        serializer = DoersClientsSerializer(dc, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DoersClientsSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def doersclients_detail(request, pk):
    try:
        dc = DoersClients.objects.get(pk=pk)
    
    except DoersClients.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = DoersClientsSerializer(dc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)        
        serializer = DoersClientsSerializer(dc, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dc.delete()
        return HttpResponse(status=204)
        

