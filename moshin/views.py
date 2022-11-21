from django.shortcuts import render
from .models import *

def bmw(request):
    posts = Bmw.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, 'moshin.html', context)

def kia(request):
    posts = Kia.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, 'moshin.html', context)

def ferreri(request):
    posts = Ferrari.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, 'moshin.html', context)

def chevrolet(request):
    posts = Chevrolet.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, 'moshin.html', context)

def honda(request):
    posts = Honda.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, 'moshin.html', context)











