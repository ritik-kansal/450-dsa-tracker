from django.db.models import fields
from webapp import models
from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=30)
    # user_name = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    # linkedin = serializers.CharField(max_length=255)
    # github = serializers.CharField(max_length=255)
    # password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self,validate_data):
        return User.objects.create(**validate_data)