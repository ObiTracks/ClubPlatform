from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=40)
    date_created =
    

class Club(models.Model):
    name = models.CharField(max_length=40)
    president = models.CharField(max_length=40)
    who_are_we = models.
    mission_statement = models.
    vision = models.
    objectives = models.
    description = models.
    history = models.
    email = models.
    discord_link = models.
    slack_link = models.
    facebook_link = models.
    instagram_link = models.
    twitter_link = models.
    linkedin_link = models.
    shared_calendar_link = models.


class Event(models.Model):
    title = models.
    date = models.
    time = models.
    short_description = models.
    long_description = models.
    location = models.
    type (choice field - Hybrid, In-Person, Remote) = models.
    rsvps = models.
    url =  = models.

class Post(models.Model):
    title = models.
    date = models.
    time = models.
    short_description = models.
    long_description = models.
    location = models.
    type (choice field - Hybrid, In-Person, Remote) = models.
    url = models.

class Update(models.Model):
    title = models.
    date = models.
    time = models.
    short_description = models.
    long_description = models.
    location = models.
    type (choice field - Hybrid, In-Person, Remote) = models.
    url = models.

class CommunityResource(models.Model):
    title = models.
    description = models.
    image = models.
    url = models.

class ClubInfoAndStatistics(models.Model):
    title = models.
    value = models.
    last_updated = models.

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
    role (regular member, president, vice-president, executive, department lead)
    school = models.ForeignKey(School, on_delete=SET_NULL, null=True)

class Team(models.Model):#Aka team, aka sub, aka division
    name = models.
    community_drive_url = models.
    repo_url = models.
    leader = models.
    leads (follow the leader and lead people on the team) = models.
