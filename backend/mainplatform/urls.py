from django.urls import path, include
from . import views


urlpatterns = [
    # LANDING PAGE
    path('', views.landingpageView, name='landingPage'),

    # LOGIN URLS
    path('register', views.registerView, name='register'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),


    path('home', views.homedashboardView, name='homedashboard'),
    path('clubs/<str:pk>/', views.clubdashboardView, name='home'),

]

