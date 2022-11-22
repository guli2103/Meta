from django.urls import path
from .views import *


urlpatterns = [
    path('moychechak/', moychechak),
    path('lola/', lola),
    path('atirgul/', atirgul),
    path('kaktus/', kaktus),
    path('binafsha/', binafsha),

]
