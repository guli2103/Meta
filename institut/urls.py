from django.urls import path
from .views import *


urlpatterns = [
    path('navoiy/', navoiy),
    path('buxoro/', buxoro),
    path('navoiy1/', navoiy1),
    path('toshkent/', toshkent),
    path('toshkent1/', toshkent1),
]
