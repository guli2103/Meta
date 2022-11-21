from django.shortcuts import render
from .models import *

def yangilik1(request):
    posts = Yangilik1.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'yangilik.html', context)

def yangilik2(request):
    posts = Yangilik1.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'yangilik.html', context)

def yangilik3(request):
    posts = Yangilik1.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'yangilik.html', context)

def yangilik4(request):
    posts = Yangilik1.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'yangilik.html', context)

def yangilik5(request):
    posts = Yangilik1.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'yangilik.html', context)




