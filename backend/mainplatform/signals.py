from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, first_name=instance.first_name, last_name=instance.last_name)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# This signal creates a relationship between a club and school
@receiver(post_save, sender=Club)
def save_profile(sender, instance, **kwargs):
    if instance.school != None:
        relationship = ClubSchoolRelationship(
            club=instance, school=instance.school)
        relationship.save()
