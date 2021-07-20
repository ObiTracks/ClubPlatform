from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    date_created = models.DateTimeField()
    
    def __str__(self):
        return self.name
    

class Club(models.Model):
    name = models.CharField(max_length=100)
    # president = models.ForeignKey(to, on_delete)
    who_are_we = models.TextField(max_length=1000)
    mission_statement = models.TextField(max_length=1000)
    vision = models.TextField(max_length=1000)
    objectives = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    history = models.TextField(max_length=1000)
    email = models.CharField(max_length=60)
    discord_link = models.CharField(max_length=100)
    slack_link = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100)
    instagram_link = models.CharField(max_length=100)
    twitter_link = models.CharField(max_length=100)
    linkedin_link = models.CharField(max_length=100)
    shared_calendar_link = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField() #Autoadd field

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    short_description = models.TextField(max_length=1000)
    long_description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    location_type =  (
        ('HB', 'Hybrid'),
        ('IP', 'In-Person'),
        ('R', 'Remote'),
    )
    # rsvps = models.ManyToManyField(to) #Many to Many relation with member objects to see who and how many rsvp'd
    url =  models.CharField(max_length=100)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.title

class Member(models.Model):
    first_name = models.CharField(max_length=40) 
    last_name = models.CharField(max_length=40)
    year_level = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
    )
    role = (
        ('M', 'Member'),
        ('TL', 'Team Lead'),
        ('E', 'Executive'),
        ('VP', 'Vice President'),
        ('P', 'President'),
    )
    school = models.ForeignKey(School, on_delete=SET_NULL, null=True)
    date_created = models.DateTimeField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# class Post(models.Model):
#     title = models.
#     date = models.
#     time = models.
#     short_description = models.
#     long_description = models.
#     location = models.
#     type (choice field - Hybrid, In-Person, Remote) = models.
#     url = models.

# class Update(models.Model):
#     title = models.
#     date = models.
#     time = models.
#     short_description = models.
#     long_description = models.
#     location = models.
#     type (choice field - Hybrid, In-Person, Remote) = models.
#     url = models.

# class CommunityResource(models.Model):
#     title = models.
#     description = models.
#     image = models.
#     url = models.

# class ClubInfoAndStatistics(models.Model):
#     title = models.
#     value = models.
#     last_updated = models.



# class Team(models.Model):#Aka team, aka sub, aka division
#     name = models.
#     community_drive_url = models.
#     repo_url = models.
#     leader = models.
#     leads (follow the leader and lead people on the team) = models.
