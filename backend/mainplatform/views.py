from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


def signupView(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            loginView(request)

            return redirect('homedashboard')
    else:
        register_form = UserRegisterForm()

    context = {'register_form': register_form}

    return render(request, '../templates/signup.html', context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, '../templates/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('landingpage')


# Home Dashboard
def landingpageView(request):
    context = {
    }

    template_name = '../templates/landingpage.html'

    return render(request, template_name, context)


def homedashboardView(request):
    usersClubs = request.user.profile.clubs.all()
    allClubs = Club.objects.all()

    page_title = "Home"
    context = {
        'page_title': page_title,
        'usersClubs': usersClubs,
        'allClubs': allClubs
    }

    template_name = '../templates/homedashboard.html'
    print(request.user.first_name)

    return render(request, template_name, context)

# Club Dashboard


def clubdashboardView(request, pk):
    profile = request.user.profile
    club = Club.objects.get(id=pk)
    usersClubs = profile.clubs.all()

    clubrelationship = request.user.profile.clubprofilerelationship_set.filter(
        club=club).first()
    events = club.event_set.all()[:7]
    posts = club.post_set.all()[:7]
    updates = club.update_set.all()[:7]
    members = club.profile_set.all()
    info = club.get_club_info()
    print(club)
    print("Total Members: ", club.get_total_members())
    print("Total Posts: ", club.get_total_posts())
    print("Total Events: ", club.get_total_events())
    print("Total Admins: ", club.get_total_admin_members())
    print("Get School: ", club.get_school())
    print("Get School Verification: ", club.get_school_verification())
    # print("Get Verification: ", club.get_verification())
    print(members)

    # event_form = None
    # post_form = None
    # update_form = None

    if request.method == 'POST':
        form_type = request.POST.get("form_type")
        form = None

        if form_type == "club_event":
            form = EventForm(request.POST)
        elif form_type == "club_post":
            form = PostForm(request.POST)
        elif form_type == "club_update":
            form = UpdateForm(request.POST)
        elif form_type == "profile":
            print(form_type)
            form = ProfileUpdateForm(
                request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.success(request, f'Form saved')

            # return redirect('club')
    # else:
    event_form = EventForm(initial={
        'club': club,
        'author': request.user.profile
    })
    post_form = PostForm(initial={
        'club': club,
        'author': request.user.profile
    })
    update_form = UpdateForm(initial={
        'club': club,
        'author': request.user.profile
    })
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    page_title = "Home"
    context = {
        'profile': profile,
        'club': club,

        'clubrelationship': clubrelationship,
        'usersClubs': usersClubs,
        'page_title': page_title,
        'events': events,
        'posts': posts,
        'updates': updates,
        'members': members,
        'info': info,

        'event_form': event_form,
        'post_form': post_form,
        'update_form': update_form,
        'profile_form': profile_form

    }

    template_name = '../templates/clubdashboard.html'

    return render(request, template_name, context)
