from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from djoser.signals import user_activated
# Create your models here.

class User(AbstractUser):
  email = models.EmailField(verbose_name='email', max_length=200, unique=True)
  username = models.CharField(verbose_name='username', max_length=200, unique=True)
  phone = models.CharField(null=True, max_length=200)
  REQUIRED_FIELDS = ['username','first_name','last_name']
  USERNAME_FIELD = 'email'

  def get_username(self):
    return self.email

