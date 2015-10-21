from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect as redirect
from django.shortcuts import render

def index(request):
    return render(request, 'recordstore/index.html', {});

def detail(request, pk):
    context = {
        'key' : pk,
        'list' : range(5),
    }
    return render(request, 'recordstore/detail.html', context);

def login_view(request):
    context = {
        'form' : AuthenticationForm(),
    }
    return render(request, 'recordstore/login.html', context)

@login_required(login_url='/recordstore/login')
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

    return redirect(reverse('recordstore:index', args=[]))
