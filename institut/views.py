from django.shortcuts import render
from .models import *


def navoiy(request):
    posts = Navoiy.objects.all()
    context ={
        'posts' : posts
    }
    return render(request, 'institut.html', context)

def buxoro(request):
    posts = Buxoro.objects.all()
    context ={
        'posts' : posts
    }
    return render(request, 'institut.html', context)

def navoiy1(request):
    posts = Navoiy1.objects.all()
    context ={
        'posts' : posts
    }
    return render(request, 'institut.html', context)

def toshkent(request):
    posts = Toshkent.objects.all()
    context ={
        'posts' : posts
    }
    return render(request, 'institut.html', context)

def toshkent1(request):
    posts = Toshkent1.objects.all()
    context ={
        'posts' : posts
    }
    return render(request, 'institut.html', context)














