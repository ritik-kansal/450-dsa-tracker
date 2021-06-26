import json
from django.shortcuts import render
from rest_framework import serializers
from ..models import *
from ..serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status,generics, permissions
from rest_framework.views import APIView
from knox.models import AuthToken
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login

# from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView