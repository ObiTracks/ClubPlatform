from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL, DO_NOTHING
from django.contrib.auth.models import User
from django.dispatch import receiver

import re
# Create your models here.


class School(models.Model):
    class Meta:
        ordering = ['-date_created']

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Club(models.Model):
    class Meta:
        ordering = ['-date_created']

    owner = models.ForeignKey('Profile', unique=False,
                              on_delete=DO_NOTHING, default=None)
    school = models.ForeignKey(
        School, on_delete=models.DO_NOTHING, null=True, blank=True)

    name = models.CharField(max_length=100)
    abv = models.CharField(max_length=4, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    email = models.CharField(max_length=60)
    # president = models.ForeignKey(to, on_delete)
    who_are_we = models.TextField(max_length=1000, blank=True)
    mission_statement = models.TextField(max_length=1000, blank=True)
    vision = models.TextField(max_length=1000, blank=True)
    objectives = models.TextField(max_length=1000, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    history = models.TextField(max_length=1000, blank=True)
    # Link to only to one discord server
    # The admin of the server must get the server ID from the widget tab in the server settings
    discord_link = models.CharField(max_length=1000, blank=True)
    slack_link = models.CharField(max_length=1000, blank=True)
    facebook_link = models.CharField(max_length=1000, blank=True)
    twitter_link = models.CharField(max_length=1000, blank=True)
    # Ex. https://www.instagram.com/laurier.cs/
    instagram_link = models.CharField(max_length=1000, blank=True)
    linkedin_link = models.CharField(max_length=1000, blank=True)
    # Provide the email address for the calendar they want shared
    shared_calendar_link = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now=True)  # Autoadd field

    def save(self, *args, **kwargs):
        # Parsing the facebook link
        if len(self.facebook_link.split("/")) != 1:
            list = self.facebook_link.split("/")
            list = [x for x in list if x != ""]
            self.facebook_link = list[-1]

        # Parsing the twitter link
        if len(self.twitter_link.split("/")) != 1:
            list = self.twitter_link.split("/")
            list = [x for x in list if x != ""]
            self.twitter_link = list[-1]

        if "%40" not in self.shared_calendar_link.split("/"):
            self.shared_calendar_link = self.shared_calendar_link.replace(
                "@", '%40')

        super().save(*args, **kwargs)

    def get_total_members(self):
        return self.clubprofilerelationship_set.count()

    def get_total_posts(self):
        return self.post_set.count()

    def get_total_events(self):
        return self.event_set.count()

    def get_total_updates(self):
        return self.school

    def get_school(self):
        return self.school

    def get_total_admin_members(self):
        adminset = self.clubprofilerelationship_set.filter(
            post_privledges=True)
        if adminset:
            return adminset.count()

    def get_school_verification(self):
        schoolrelationship = self.clubschoolrelationship_set.first()
        if schoolrelationship:
            return schoolrelationship.verified

    def get_club_statistics(self):
        info = {
            "Members": self.get_total_members(),
            "Total Admin": self.get_total_admin_members(),
            "Total Events Hosted": self.get_total_events(),
            "School": self.get_school(),
            "School Verified": self.get_school_verification()
        }

        return info

    def get_club_social_links(self):
        socials = {
            "Instagram": self.instagram_link,
            "LinkedIn": self.linkedin_link,
            "Email": self.email
        }

        return socials

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(
        School, null=True, blank=True, on_delete=models.DO_NOTHING)

    YEAR_LEVEL = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
        ('5', 'Fifth'),
        ('NA', 'Not Applicable'),
    )
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    year_level = models.CharField(
        max_length=40, choices=YEAR_LEVEL, default='M')
    image = models.ImageField(
        upload_to='images/', default=None, null=True, blank=True)

    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class ClubSchoolRelationship(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, unique=False)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, unique=False)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)  # Autoadd field

    def __str__(self):
        return "{} - {}".format(self.school.name, self.club.name, )


class ClubProfileRelationship(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, unique=False)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, unique=False)
    post_privledges = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)  # Autoadd field

    ROLE = (
        ('M', 'Member'),
        ('TL', 'Team Lead'),
        ('S', 'Staff'),
        ('E', 'Executive'),
        ('VP', 'Vice President'),
        ('P', 'President'),
    )
    role = models.CharField(max_length=40, choices=ROLE, default='M')

    def __str__(self):
        return "{} - {} {}".format(self.club.name, self.profile.first_name, self.profile.last_name)


class Event(models.Model):
    class Meta:
        ordering = ['-date_created']

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    LOCATION_TYPE = (
        ('HB', 'Hybrid'),
        ('IP', 'In-Person'),
        ('R', 'Remote'),
    )
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, default=None, null=True)
    short_description = models.TextField(
        max_length=1000, verbose_name="caption")
    long_description = models.TextField(
        max_length=1000, verbose_name="description", blank=True)
    location = models.CharField(
        max_length=100, blank=False, choices=LOCATION_TYPE, default='R')
    physical_location = models.CharField(max_length=100, blank=True)

    # rsvps = models.ManyToManyField(to) #Many to Many relation with Profile objects to see who and how many rsvp'd
    url = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta:
        ordering = ['-date_created']

    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    LOCATION_TYPE = (
        ('HB', 'Hybrid'),
        ('IP', 'In-Person'),
        ('R', 'Remote'),
    )
    date = models.DateTimeField(blank=True, default=None, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100, blank=True)
    long_description = models.CharField(max_length=100, blank=True)
    location = models.CharField(
        max_length=150, blank=True, choices=LOCATION_TYPE)
    url = models.CharField(max_length=1000, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ("{}".format(self.title, self.date))


class Update(models.Model):
    class Meta:
        ordering = ['-date_created']

    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    PRIORITY_LEVEL = (
        # ('VH', 'Very High'),
        ('H', 'High'),
        ('R', 'Regular'),
    )
    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, default=None)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=1000, blank=True)
    priority_level = models.CharField(
        max_length=150, blank=True, choices=PRIORITY_LEVEL, default='R')
    date_created = models.DateTimeField(auto_now=True)


class Pod(models.Model):  # Aka team, aka sub, aka division, aka Pods
    pod_lead = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None)

    name = models.CharField(max_length=100)
    community_drive_url = models.CharField(max_length=100, blank=True)
    repo_url = models.CharField(max_length=100, blank=True)
    external_url = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now=True)  # Autoadd field


class Resource(models.Model):
    class Meta:
        ordering = ['-date_created']

    club = models.ForeignKey(Club, on_delete=models.CASCADE, default=None)
    pod = models.ForeignKey(Pod, on_delete=models.CASCADE, default=None)

    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, default=None)
    time = models.DateTimeField()
    url = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now=True)
    RESOURCE_TYPE = (
        ('G', 'Community Game'),
        ('LV', 'Learning Video'),
        ('LD', 'Learning Document'),
        ('D', 'Documentation'),
        ('U', 'Useful Resource'),
        ('S', 'School Resource'),
    )
    resource_type = models.CharField(
        max_length=150, blank=True, choices=RESOURCE_TYPE)
