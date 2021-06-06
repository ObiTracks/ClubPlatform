from django.db import models

class School(models.Model):
    name = models.CharField()
    email = models.CharField()
    def _str_(self):
        return self.title


class Club(models.Model):
    name
    school
    president
    total_members
    date_founded
    social_media_links
    created_at
    certified

class Stats(models.Model):
    total_members
    total_leadership
    total_projects

class Division(models.Model):
    name
    description
    created_at
    club


class Role(models.Model):
    name
    responsibilities

class Member(models.Model):
    first_name
    last_name
    email
    position

class Post(models.Model):
    title
    text
    created_at
    author
    club

# class Project(models.Model): (for ongoing projects within a club)


# Create your models here.
class Club(models.Model):
    title = models.CharField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title