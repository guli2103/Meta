from django.urls import path
from .views import *


urlpatterns = [
    path('telefon/', infinix),
    path('telefon/', samsung),
    path('telefon/', apple),
    path('telefon/', redme),
    path('telefon/', vivo),
]