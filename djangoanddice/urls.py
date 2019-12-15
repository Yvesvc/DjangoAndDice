
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('', include('sheet.urls')),
    path('spells/', include('spells.urls')),
    path('equipment/', include('equipment.urls')),
    path('info/', include('info.urls'))
]
