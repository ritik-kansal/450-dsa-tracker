from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    linkedin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    password = models.CharField(max_length=255)