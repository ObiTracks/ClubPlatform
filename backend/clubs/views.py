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

class EventView(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

class MemberView(viewsets.ModelViewSet):
  queryset = Member.objects.all()
  serializer_class = MemberSerializer

class PostView(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UpdateView(viewsets.ModelViewSet):
  queryset = Update.objects.all()
  serializer_class = UpdateSerializer

class ResourceView(viewsets.ModelViewSet):
  queryset = Resource.objects.all()
  serializer_class = ResourceSerializer

