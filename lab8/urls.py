from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokedex/', include('pokedex.urls')),
    path('', lambda request: redirect('/pokedex/')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
