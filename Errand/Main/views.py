from django.shortcuts import render
from django.http import HttpResponse
from .models import Offer
from  .models import List, Public

def home(request):
    return render(request, 'index.html')


def about(request):
    publics = Public.objects.all()
    return render(request, 'about.html', {'publics':publics})


def service(request):
    offers = Offer.objects.all()

    return render(request, 'service.html', {'offers':offers})

def outline(request):
    lists = List.objects.all()

    return render(request, 'outline.html', {'lists':lists})

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')