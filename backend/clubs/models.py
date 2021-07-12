from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=40)
    manager = models.CharField(max_length=40) 

class School(models.Model):
    name = models.CharField(max_length=40)
    clubs = models.ManyToManyField(Club)

class Member(models.Model):
    first_name = models.CharField(max_length=40) 
    last_name = models.CharField(max_length=40)
    YEAR_LEVEL = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
    )
    school = models.ForeignKey(School, on_delete=SET_NULL, null=True)