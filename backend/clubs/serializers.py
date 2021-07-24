from rest_framework import serializers
from .models import Club

class ClubSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Club
    fields = ('id', 'url', 'name', 'email', 'who_are_we', 'mission_statement', 'vision', 'objectives', 'description')