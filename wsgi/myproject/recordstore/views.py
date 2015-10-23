from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .forms import *

def home(request):
    return render(request, 'recordstore/index.html', {});

# 
# views related to logging in and out
#

def login_view(request):
    context = {
        'form' : AuthenticationForm(),
        'next' : request.GET.get('next', ''),
    }
    return render(request, 'recordstore/login.html', context)

def logout_view(request):
    name = request.user.username
    logout(request)
    context = {
        'name' : name,
    }
    return render(request, 'recordstore/logout.html', context)

def authenticate_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return redirect(reverse('recordstore:login', args=[]))

    next_url = request.POST.get('next', '')
    if len(next_url) == 0:
        return redirect(reverse('recordstore:home', args=[]))
    else:
        return redirect(next_url)

#
# Album and Pressing-centric view
#

def all_records(request):
    records = Album.objects.all()
    context = {
        'records' : records,
    }
    return render(request, 'recordstore/all_records.html', context)

class AlbumDetailView(DetailView):
    model = Album

class PressingDetailView(DetailView):
    model = Pressing

#
# Artist-centric view
#

class ArtistListView(ListView):
    model = Artist

class ArtistDetailView(DetailView):
    model = Artist

@login_required
def create_artist(request):
    context = {
        'artist_form' : ArtistForm()
    }
    return render(request, 'recordstore/create_artist.html', context)
