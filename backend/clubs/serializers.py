from rest_framework import serializers
from .models import *

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = School
    fields = "__all__"

class ClubSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Club
    fields = "__all__"

class EventSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Event
    fields = "__all__"

class MemberSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Member
    fields = "__all__"

class PostSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"

class UpdateSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Update
    fields = "__all__"

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Resource
    fields = "__all__"

