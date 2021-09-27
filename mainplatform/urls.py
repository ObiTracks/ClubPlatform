from django.urls import path, include
from . import views


urlpatterns = [
    # LANDING PAGE
    path('', views.landingpageView, name='landingpage'),

    # LOGIN URLS
    path('signup', views.signupView, name='signup'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),


    path('home', views.homedashboardView, name='home'),
    path('clubs/<str:pk>/', views.clubdashboardView, name='club'),
    path('clubs/<str:pk>/events', views.eventsView, name='events'),
    path('clubs/<str:pk>/posts', views.postsView, name='posts'),
    path('clubs/<str:pk>/updates', views.updatesView, name='updates'),
    path('delete/<str:type>/<str:pk>', views.deleteView, name='delete'),
]
