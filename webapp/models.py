from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError("username not valid")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,is_active=is_active,is_staff=is_staff,is_superuser=is_superuser,date_joined=now,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,username,email,password,**extra_fields):
        # change
        return self._create_user(username,email,password,**extra_fields)

    def create_superuser(self,username,email,password,**extra_fields):
        # change
        return self._create_user( username, email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField()
    first_name = None
    last_name = None
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30,unique=True)
    linkedin = models.CharField(max_length=255,blank=True,null=True)
    github = models.CharField(max_length=255,blank=True,null=True)
    # password = models.CharField(max_length=255)
    # inherited from base class

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email',]

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

    class Meta:
        unique_together = ('user_1','user_2')

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

    class Meta:
        unique_together = ('question_id','user_id')

class Mark_update(models.Model):
    marks = [
        (0,"pending"),
        (1,"need to revise"),
        (2,"done"),
    ]
    previous_mark = models.IntegerField(choices=marks,default=0,
            validators=[
                MaxValueValidator(2),
                MinValueValidator(0)
            ]
        )
    question_user_mark_id = models.ForeignKey(
        'Question_user_mark',
        on_delete=models.CASCADE,
        db_column='question_user_mark_id'
    )
    updated_at = models.DateTimeField(auto_now_add=True)
