from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gul/',include('gul.urls')),
    path('institut/',include('institut.urls')),
    path('moshin/', include('moshin.urls')),
    path('telefon/', include('telefon.urls')),
    path('yangilik/', include('yangilik.urls')),
]
