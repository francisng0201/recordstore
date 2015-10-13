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
