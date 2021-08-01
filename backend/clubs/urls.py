from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('schools', views.SchoolView)
router.register('clubs', views.ClubView)
router.register('events', views.EventView)
router.register('members', views.MemberView)
router.register('posts', views.PostView)
router.register('updates', views.UpdateView)
router.register('resources', views.ResourceView)

urlpatterns = [
    path('', include(router.urls))
]

