from django.apps import apps
from clubs.models import Club
from django.contrib import admin

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
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass