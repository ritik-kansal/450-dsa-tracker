"""dsa_450_tracker_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views
from webapp.views import *
from knox import views as knox_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users', UserApi.as_view()),
    path('api/users/<int:id>', UserApi.as_view()),

    path('api/questions', QuestionApi.as_view()),
    path('api/questions/<int:id>', QuestionApi.as_view()),
    
    path('api/topics', TopicApi.as_view()),
    path('api/topics/<int:id>', TopicApi.as_view()),
    
    path('api/register', RegisterAPI.as_view(), name='register'),
    path('api/login', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
