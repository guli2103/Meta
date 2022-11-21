from django.shortcuts import render
from .models import *

def infinix(request):
    posts = Infinix.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'telefon.html', context)


def samsung(request):
    posts = Samsung.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'telefon.html', context)


def apple(request):
    posts = Apple.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'telefon.html', context)


def redme(request):
    posts = Redme.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'telefon.html', context)


def vivo(request):
    posts = Vivo.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'telefon.html', context)










