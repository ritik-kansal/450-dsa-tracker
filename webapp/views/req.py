import json
from django.shortcuts import render
from rest_framework import serializers
from ..models import *
from ..serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt