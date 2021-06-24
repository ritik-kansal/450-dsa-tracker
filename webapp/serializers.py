from django.db.models import fields
from webapp import models
from rest_framework import serializers
from .models import *
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True) 
    # last_name = serializers.CharField(required=False, write_only=True)
    # address = serializers.CharField(required=False, write_only=True)

    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('first_name', ''),
            'user_name': self.validated_data.get('last_name', ''),
            # 'address': self.validated_data.get('address', ''),
            # 'user_type': self.validated_data.get('user_type', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

# class UserSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField(max_length=30)
#     # user_name = serializers.CharField(max_length=30)
#     # email = serializers.EmailField()
#     # linkedin = serializers.CharField(max_length=255)
#     # github = serializers.CharField(max_length=255)
#     # password = serializers.CharField(max_length=255)
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}
    
    # def create(self,validate_data):
    #     return User.objects.create(**validate_data)

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