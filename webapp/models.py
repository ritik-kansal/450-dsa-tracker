from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    linkedin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

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
