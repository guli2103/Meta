from django.shortcuts import render
from .models import *


def moychechak(request):
    posts = Moychechak.objects.all()
    context = {
        'posts' : posts 
    }
    return render(request, 'gul.html', context)

def lola(request):
    posts = Lola.objects.all()
    context = {
        'posts' : posts 
    }
    return render(request, 'gul.html', context)    

def atirgul(request):
    posts = Atirgul.objects.all()
    context = {
        'posts' : posts 
    }
    return render(request, 'gul.html', context)

def kaktus(request):
    posts = Kaktus.objects.all()
    context = {
        'posts' : posts 
    }
    return render(request, 'gul.html', context)

def binafsha(request):
    posts = Binafsha.objects.all()
    context = {
        'posts' : posts 
    }
    return render(request, 'gul.html', context)





