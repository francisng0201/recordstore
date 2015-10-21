from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'recordstore/index.html', {});

def detail(request, pk):
    context = {
        'key' : pk,
        'list' : range(5),
    }
    return render(request, 'recordstore/detail.html', context);

def login(request):
    context = {
        'form' : AuthenticationForm()
    }
    return render(request, 'recordstore/login.html', context)

def authenticate(request):
    username = request.post['username']
    password = request.post['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        pass

    return redirect(reverse('recordstore:index', args=[]))
