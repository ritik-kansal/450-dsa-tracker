from django.db.models import fields
from webapp import models
from rest_framework import serializers
from .models import *
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email, user_username

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
    def validate(self, data):
        """
        cant create superuser or staff via api
        """
        if "is_staff" in data or "is_superuser" in data:
            raise serializers.ValidationError({"roles":"can not create superuser or staff via api"})
        return data
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'    
    def create(self,validate_data):
        return Question.objects.create(**validate_data)
        
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'    
    def create(self,validate_data):
        return Topic.objects.create(**validate_data)

class QuestionUserMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_user_mark
        exclude = ('user_id',)
        # fields='__all__'
    def create(self,validate_data):
        return Question_user_mark.objects.create(**validate_data)

class PairProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair_programmer
        fields = '__all__'    
    def create(self,validate_data):
        return Pair_programmer.objects.create(**validate_data)

class UserAskedForPairProgrammingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_asked_for_pair_programming
        fields = '__all__'    
    def create(self,validate_data):
        return User_asked_for_pair_programming.objects.create(**validate_data)

class MarkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark_update
        fields = '__all__'    
    def create(self,validate_data):
        return Mark_update.objects.create(**validate_data)