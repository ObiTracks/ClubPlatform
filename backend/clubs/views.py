from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .models import *
from .serializers import *

class SchoolView(viewsets.ModelViewSet):
  queryset = School.objects.all()
  serializer_class = SchoolSerializer

class ClubView(viewsets.ModelViewSet):
  queryset = Club.objects.all()
  serializer_class = ClubSerializer

