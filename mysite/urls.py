from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('gouni/', admin.site.urls),
    path('', include('core.urls'))
]
