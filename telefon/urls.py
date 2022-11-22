from django.urls import path
from .views import *


urlpatterns = [
    path('infinix/', infinix),
    path('samsung/', samsung),
    path('apple/', apple),
    path('redme/', redme),
    path('vivo/', vivo),
]