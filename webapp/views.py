import json
from django.shortcuts import render
from rest_framework import serializers
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# get user
def user_detail(request,id):
    user_data = User.objects.get(id=id)  
    serializer = UserSerializer(user_data)
    return JsonResponse(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")

def all_user_detail(request):
    user_data = User.objects.all()  
    serializer = UserSerializer(user_data, many=True)
    return JsonResponse(serializer.data, safe=False)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
# get user


# create user
@csrf_exempt
def user_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = UserSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'user created'}
            return JsonResponse(res)
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(serializer.errors)
    res = {'msg':'error occured'}
    return JsonResponse(res)
# create user