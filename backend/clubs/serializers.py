from rest_framework import serializers
from .models import *

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = School
    fields = "__all__"

class ClubSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Club
    fields = ('id', 'url', 'name', 'email', 'who_are_we', 'mission_statement', 'vision', 'objectives', 'description')