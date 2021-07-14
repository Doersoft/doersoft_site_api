from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from doerscareer.models import CareerCategory, Career, CareerForm
from doerscareer.serializers import CareerCategorySerializer, CareerSerializer, CareerFormSerializer
from rest_framework.response import Response

@csrf_exempt
def CareerCategory_list(request):
    """
    List all doerscareercategory list, or create a new snippet.
    """
    if request.method == 'GET':
        cc = CareerCategory.objects.all()
        serializer = CareerCategorySerializer(cc, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CareerCategorySerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def CareerCategory_detail(request, pk):
    try:
        cc = CareerCategory.objects.get(pk=pk)
    
    except CareerCategory.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CareerCategorySerializer(cc)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)        
        serializer = CareerCategorySerializer(cc, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cc.delete()
        return HttpResponse(status=204)

''' Career Model related views'''

@csrf_exempt
def Career_list(request):
    """
    List all doerscareer list, or create a new snippet.
    """
    if request.method == 'GET':
        c = Career.objects.all()
        serializer = CareerSerializer(c, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CareerSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Career_detail(request, pk):
    try:
        c = Career.objects.get(pk=pk)
    
    except Career.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CareerSerializer(c)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)        
        serializer = CareerSerializer(c, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        c.delete()
        return HttpResponse(status=204)
        

''' CareerForm Model related views'''

@csrf_exempt
def CareerForm_list(request):
    """
    List all doerscareerform list, or create a new snippet.
    """
    if request.method == 'GET':
        cf = CareerForm.objects.all()
        serializer = CareerFormSerializer(cf, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CareerFormSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def CareerForm_detail(request, pk):
    try:
        cf = CareerForm.objects.get(pk=pk)
    
    except CareerForm.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CareerFormSerializer(cf)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)        
        serializer = CareerFormSerializer(cf, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cf.delete()
        return HttpResponse(status=204)
        

