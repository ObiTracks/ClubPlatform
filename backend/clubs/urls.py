from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('schools', views.SchoolView)
router.register('clubs', views.ClubView)

urlpatterns = [
    path('', include(router.urls))
]

