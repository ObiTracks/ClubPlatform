from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL, DO_NOTHING

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    date_created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Club(models.Model):
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True, blank=True)

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    # president = models.ForeignKey(to, on_delete)
    who_are_we = models.TextField(max_length=1000, blank=True)
    mission_statement = models.TextField(max_length=1000, blank=True)
    vision = models.TextField(max_length=1000, blank=True)
    objectives = models.TextField(max_length=1000, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    history = models.TextField(max_length=1000, blank=True)
    discord_link = models.CharField(max_length=1000, blank=True)
    slack_link = models.CharField(max_length=1000, blank=True)
    facebook_link = models.CharField(max_length=1000, blank=True)
    instagram_link = models.CharField(max_length=1000, blank=True)
    twitter_link = models.CharField(max_length=1000, blank=True)
    linkedin_link = models.CharField(max_length=1000, blank=True)
    shared_calendar_link = models.CharField(max_length=1000, blank=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True) #Autoadd field

    def __str__(self):
        return self.name

class Member(models.Model):
    school = models.ForeignKey(School, null=True, on_delete=models.DO_NOTHING)
    clubs = models.ManyToManyField(Club, default=None, blank=True)

    YEAR_LEVEL = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('NA', 'Not Applicable'),
    )
    ROLE = (
        ('M', 'Member'),
        ('TL', 'Team Lead'),
        ('E', 'Executive'),
        ('VP', 'Vice President'),
        ('P', 'President'),
    )
    first_name = models.CharField(max_length=40) 
    last_name = models.CharField(max_length=40)
    year_level = models.CharField(max_length=40, choices=YEAR_LEVEL, default='M')
    role = models.CharField(max_length=40, choices=ROLE, default='M')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    
    LOCATION_TYPE =  (
        ('HB', 'Hybrid'),
        ('IP', 'In-Person'),
        ('R', 'Remote'),
    )
    title = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    short_description = models.TextField(max_length=1000)
    long_description = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=100, blank=False, choices=LOCATION_TYPE, default='R')
    physical_location = models.CharField(max_length=100, blank=True)

    # rsvps = models.ManyToManyField(to) #Many to Many relation with member objects to see who and how many rsvp'd
    url =  models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)

    LOCATION_TYPE =  (
        ('HB', 'Hybrid'),
        ('IP', 'In-Person'),
        ('R', 'Remote'),
    )
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField()
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=150, blank=True, choices=LOCATION_TYPE)
    url = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title, self.date)

class Update(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    
    PRIORITY_LEVEL =  (
        ('H', 'High'),
        ('R', 'Regular')
    )
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField()
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=100, blank=True)
    external_url = models.CharField(max_length=1000)
    priority_level = models.CharField(max_length=150, blank=True, choices=PRIORITY_LEVEL, default='R')
    date_created = models.DateTimeField(auto_now=True)
    
class Pod(models.Model):#Aka team, aka sub, aka division, aka Pods
    pod_lead = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)

    name = models.CharField(max_length=100)
    community_drive_url = models.CharField(max_length=100, blank=True)
    repo_url = models.CharField(max_length=100, blank=True)
    external_url = models.CharField(max_length=100, blank=True)


class Resource(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, default=None)

    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField()
    url = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)
    RESOURCE_TYPE =  (
        ('G', 'Community Game'),
        ('LV', 'Learning Video'),
        ('LD', 'Learning Document'),
        ('D', 'Documentation'),
        ('U', 'Useful Resource'),
        ('S', 'School Resource'),
    )
    resource_type = models.CharField(max_length=150, blank=True, choices=RESOURCE_TYPE)

    
