from typing import AbstractSet
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30,unique=True)
    email = models.EmailField()
    linkedin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()


class Topic(models.Model):
    name = models.CharField(max_length=100)

class Question(models.Model):
    levels = [
        (0,"easy"),
        (1,"medium"),
        (2,"hard")
    ]
    name = models.CharField(max_length=200)
    link = models.URLField()
    level = models.IntegerField(choices=levels,validators=[
            MaxValueValidator(2),
            MinValueValidator(0)
        ])

    topic_id = models.ForeignKey(
        'Topic',
        to_field='id',#even if not mentioned django use primary key as to_field 
        on_delete=models.CASCADE,
        db_column='topic_id' #django automatically appends _id i.e we could have used topic in model and in database django automatically creates topic_id (https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey)
    )

    def __str__(self):
        return self.link

class Pair_programmer(models.Model):
    user_1 = models.ForeignKey(
        'User',
        # not mentioning to_field
        on_delete=models.CASCADE,
        db_column='user_1',
        related_name='%(class)s_user_1'
    )
    user_2 = models.ForeignKey(
        'User',
        # not mentioning to_field
        on_delete=models.CASCADE,
        db_column='user_2',
        related_name='%(class)s_user_2'
    )

class User_asked_for_pair_programming(models.Model):
    user_id = models.ForeignKey(
        'User',
        # not mentioning to_field
        on_delete=models.CASCADE,
        db_column='user_id',
    )

class Question_user_mark(models.Model):
    marks = [
        (0,"pending"),
        (1,"need to revise"),
        (2,"done"),
    ]
    user_id = models.ForeignKey(
        'User',
        # not mentioning to_field
        on_delete=models.CASCADE,
        db_column='user_id',
    )
    question_id = models.ForeignKey(
        'Question',
        # not mentioning to_field
        on_delete=models.CASCADE,
        db_column='question_id',
    )
    mark = models.IntegerField(choices=marks,default=0,
            validators=[
                MaxValueValidator(2),
                MinValueValidator(0)
            ]
        )
    created_at = models.DateTimeField(auto_now_add=True)

class Mark_update(models.Model):
    question_user_mark_id = models.ForeignKey(
        'Question_user_mark',
        on_delete=models.CASCADE,
        db_column='question_user_mark_id'
    )
    updated_at = models.DateTimeField(auto_now_add=True)
