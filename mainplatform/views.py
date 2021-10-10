from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.http.response import HttpResponseRedirect
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
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            print("New user created")

            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        register_form = UserRegisterForm()

    context = {'register_form': register_form}

    return render(request, '../templates/signup.html', context)


def loginView(request):
    if request.user.is_authenticated:
        print("Hello")
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Logged In")
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
    usersClubs = [
        clubrelationship.club for clubrelationship in request.user.profile.clubprofilerelationship_set.all()]
    print(usersClubs)
    allClubs = Club.objects.all()

    if request.method == 'POST':
        form_type = request.POST.get("form_type")
        form = None

        if form_type == "club":
            form = ClubForm(request.POST, request.FILES)
        elif form_type == "profile":
            form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            subject = form.cleaned_data
            print("*******CLEANED DATA********")
            print(subject)
            print("*******CLEANED DATA********")

            obj = form.save()
            if form_type == "club":
                relationship = ClubProfileRelationship(
                    club=obj, profile=request.user.profile, post_privledges=True, role="P")
                relationship.save()
            return redirect('home')
        else:
            print("Form not saved")
            messages.success(request, f'Welcome to your new club!')

            # return redirect('club')
    # else:
    club_form = ClubForm(initial={
        'owner': request.user.profile
    })
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    page_title = "Home"
    context = {
        'page_title': page_title,
        'usersClubs': usersClubs,
        'allClubs': allClubs,
        'club_form': club_form,
        'profile_form': profile_form,
        'club': None
    }

    template_name = '../templates/homedashboard.html'
    # print(request.user.first_name)

    return render(request, template_name, context)

# Club Dashboard


def clubdashboardView(request, pk):
    if request.user.is_anonymous == False:
        profile = request.user.profile
    else:
        profile = None

    club = Club.objects.get(id=pk)
    usersClubs = [
        clubrelationship.club for clubrelationship in request.user.profile.clubprofilerelationship_set.all()]

    clubrelationship = request.user.profile.clubprofilerelationship_set.filter(
        club=club).first()
    events = club.event_set.all()[:7]
    posts = club.post_set.all()[:7]
    updates = club.update_set.all()[:7]
    members = [
        (relationship.profile, relationship) for relationship in club.clubprofilerelationship_set.all()]
    info = club.get_club_statistics()
    social_links = club.get_club_social_links()

    if request.method == 'POST':
        form_type = request.POST.get("form_type")
        form = None

        if form_type == "club":
            form = ClubForm(request.POST, request.FILES, instance=club)
        elif form_type == "club_event":
            form = EventForm(request.POST, request.FILES)
        elif form_type == "club_post":
            form = PostForm(request.POST, request.FILES)
        elif form_type == "club_update":
            form = UpdateForm(request.POST, request.FILES)
        elif form_type == "profile":
            form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)
            print("Profile form used")
            # prod.image = request.FILES['image']
        elif form_type == "club_relationship":
            if clubrelationship == None:
                form = ClubProfileRelationshipForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data
            print("*******CLEANED DATA********")
            print(subject)
            print("*******CLEANED DATA********")
            obj = form.save(commit=False)
            if form_type == "club_relationship":
                obj.profile = profile
            obj.save()
            print("Form saved")
            messages.success(request, f'Form saved')

            return redirect('home')

            # return redirect('club')
    # else:
    club_form = ClubForm(instance=club)
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
    clubprofilerelationship_form = ClubProfileRelationshipForm(initial={
        'club': club,
        'profile': profile
    })

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
        'social_links': social_links,

        'club_form': club_form,
        'event_form': event_form,
        'post_form': post_form,
        'update_form': update_form,
        'profile_form': profile_form,
        'clubprofilerelationship_form': clubprofilerelationship_form
    }

    template_name = '../templates/clubdashboard.html'

    return render(request, template_name, context)


def eventsView(request, pk):
    club = Club.objects.get(id=pk)
    events = club.event_set.all()
    print(events)

    page_title = "Events"
    context = {
        'page_title': page_title,
        'club': club,
        'list': events

    }

    template_name = '../templates/listView.html'

    return render(request, template_name, context)


def postsView(request, pk):
    club = Club.objects.get(id=pk)
    posts = club.event_set.all()

    page_title = "Posts"
    context = {
        'page_title': page_title,
        'club': club,
        'list': posts

    }

    template_name = '../templates/listView.html'

    return render(request, template_name, context)


def updatesView(request, pk):
    club = Club.objects.get(id=pk)
    updates = club.event_set.all()

    page_title = "Updates"
    context = {
        'page_title': page_title,
        'club': club,
        'list': updates

    }

    template_name = '../templates/listView.html'

    return render(request, template_name, context)


def deleteView(request, type: str, pk):
    if type == "Event":
        obj = Event.objects.get(id=pk)
    elif type == "Post":
        obj = Post.objects.get(id=pk)
    elif type == "Update":
        obj = Update.objects.get(id=pk)

    if obj != None:
        obj.delete()
        return redirect('home')

    return redirect('home')

    # context = {}
    # template_name = '../templates/crud_templates/delete.html'
    # return render(request, template_name, context)
