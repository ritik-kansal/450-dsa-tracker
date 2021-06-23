import json
from django.shortcuts import render
from rest_framework import serializers
from .models import User
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.
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