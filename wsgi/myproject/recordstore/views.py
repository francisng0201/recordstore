from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.defaults import bad_request 
from django.http import HttpResponseRedirect as redirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *
from .forms import *

def home(request):
    return render(request, 'recordstore/index.html', {});

# 
# logging in and out
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

def join_user(request):
    return redirect(reverse('recordstore:home', args=[]))

def create_user(request):
    return redirect(reverse('recordstore:home', args=[]))

#
# modifying/looking at a personal record collection
#

@login_required
def view_collection(request):
    return redirect(reverse('recordstore:home', args=[]))

@login_required
def view_profile(request):
    recordstore_user = get_object_or_404(RecordStoreUser, django_user_id=request.user.id)
    context = {
        'rc_user' : recordstore_user,
        'records' : recordstore_user.ownedrecord_set.all(),
    }
    return render(request, 'recordstore/view_profile.html', context)

@login_required
def add_to_collection(request):
    user = get_object_or_404(RecordStoreUser, django_user_id=request.user.id)
    album_id = request.POST.get('album_id', None)
    pressing_id = request.POST.get('pressing_id', None)

    if album_id == None or pressing_id == None:
        return bad_request(request)

    record = {
        'owner' : user.id,
        'album' : album_id,
        'pressing' : pressing_id,
    }
    form = OwnedRecordForm(record)
    form.save()

    return redirect(reverse('recordstore:view_profile', args=[]))

@login_required
def delete_collection(request):
    record_id = request.POST.get('id', None)
    OwnedRecord.objects.get(pk=record_id).delete()
    return redirect(reverse('recordstore:view_profile', args=[]))


#
# Albums
#

def all_records(request):
    records = Album.objects.all()
    context = {
        'records' : records,
    }
    return render(request, 'recordstore/all_records.html', context)

class AlbumDetailView(DetailView):
    model = Album

@login_required
def create_album(request):
    context = {
        'album_form' : AlbumForm()
    }
    return render(request, 'recordstore/create_album.html', context)

@login_required
def update_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    context = {
        'album' : album,
        'album_form' : AlbumForm(instance=album)
    }
    return render(request, 'recordstore/update_album.html', context)

@login_required
def process_album(request):
    album_id = request.POST.get('album_id', None)

    if album_id != None:
        album = get_object_or_404(Album, pk=album_id)
        album_form = AlbumForm(instance=album, data=request.POST)
    else:
        album_form = AlbumForm(request.POST)

    album_form.save()

    return redirect(reverse('recordstore:all_records', args=[]))

#
# Pressings
#

class PressingDetailView(DetailView):
    model = Pressing

@login_required
def create_pressing(request):
    context = {
        'pressing_form' : PressingForm()
    }
    return render(request, 'recordstore/create_pressing.html', context)

@login_required
def process_pressing(request):
    pressing_form = PressingForm(request.POST)
    pressing_form.save()
    return redirect(reverse('recordstore:all_records', args=[]))

#
# Artists
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

@login_required
def update_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    context = {
        'artist' : artist,
        'artist_form' : ArtistForm(instance=artist)
    }
    return render(request, 'recordstore/update_artist.html', context)

@login_required
def process_artist(request):
    artist_id = request.POST.get('artist_id', None)

    if artist_id != None:
        artist = get_object_or_404(Artist, pk=artist_id)
        artist_form = ArtistForm(instance=artist, data=request.POST)
        artist_form.save()
    else:
        artist_form = ArtistForm(request.POST)
        artist_form.save()

    return redirect(reverse('recordstore:all_artists', args=[]))

#
# Record Label-centric views
#

@login_required
def create_record_label(request):
    context = {
        'record_label_form' : RecordLabelForm()
    }
    return render(request, 'recordstore/create_record_label.html', context)

@login_required
def process_record_label(request):
    record_label_form = RecordLabelForm(request.POST)
    record_label_form.save()
    return redirect(reverse('recordstore:home', args=[]))
