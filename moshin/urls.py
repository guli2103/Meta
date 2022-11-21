from django.urls import path
from .views import *


urlpatterns = [
    path('moshin/', bmw),
    path('moshin/', kia),
    path('moshin/', ferreri),
    path('moshin/', chevrolet),
    path('moshin/', honda),
]