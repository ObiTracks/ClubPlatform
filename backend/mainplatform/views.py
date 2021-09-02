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
    return render(request, '../templates/login_templates/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
    # return redirect('home')

#Home Dashboard
def landingpageView(request):
    context = {
    }

    template_name = '../templates/homedashboard.html'

    return render(request, template_name, context)

def homedashboardView(request):
    usersClubs = request.user.profile.clubs.objects.all()
    allClubs = Club.objects.all()

    page_title = "Home"
    context = {
        'page_title': page_title,
        'users_clubs':usersClubs,
        'all_clubs': allClubs
    }

    template_name = '../templates/homedashboard.html'

    return render(request, template_name, context)

#Club Dashboard
def clubdashboardView(request, pk):
    club = Club.object.get(id=pk)
    events = club.event_set.all()[:5]
    posts = club.post_set.all()[:5]
    updates = club.update_set.all()[:5]

    page_title = "Home"
    context = {
        'page_title': page_title,
        'events':events,
        'posts': posts,
        'updates':updates
    }

    template_name = '../templates/clubdashboard.html'

    return render(request, template_name, context)