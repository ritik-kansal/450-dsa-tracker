from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.views import APIView
from knox.models import AuthToken
from rest_framework.permissions import *
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
