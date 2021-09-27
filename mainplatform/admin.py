from django.apps import apps
from django.contrib import admin
from .models import *
from django.contrib.auth.models import UserManager, AbstractUser


# Register your models here.

# Any models that need to have a customized admin, add them here.
# Otherwise, to add the rest automatically use the bottom for loop.
# This tip was gotten from https://medium.com/hackernoon/automatically-register-all-models-in-django-admin-django-tips-481382cf75e5
# class ClubAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Club._meta.get_fields()]
# admin.site.register(Club, ClubAdmin)# model registered with custom admin


# all other models
models = apps.get_models()

for model in models:
    try:
        if model.__name__ != "Club":
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


class ClubModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()

        if not ClubProfileRelationship.objects.filter(profile=request.user.profile).filter(club=obj):
            relationship = ClubProfileRelationship.objects.create(
                club=obj, profile=request.user.profile, post_privledges=True, is_owner=True, role="P")
            relationship.save()
            print("Club Relationship created")


admin.site.register(Club, ClubModelAdmin)
