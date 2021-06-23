from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    user_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    linkedin = serializers.CharField(max_length=255)
    github = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)