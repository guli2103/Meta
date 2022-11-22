from django.urls import path
from .views import *


urlpatterns = [
    path('bmw/', bmw),
    path('kia/', kia),
    path('ferrari/', ferreri),
    path('chevrolet/', chevrolet),
    path('honda/', honda),
]