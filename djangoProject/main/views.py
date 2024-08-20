from django.shortcuts import render
from django.http import HttpResponse


data = {
        'caption': "ArtDjango"
    }


# Create your views here.
def index(request):
    return render(request, 'main/index.html', data)


def new(request):
    return render(request, 'main/new.html', data)


def article(request):
    return render(request, 'main/data.html')


def test(request):
    return render(request, 'main/test.html')
