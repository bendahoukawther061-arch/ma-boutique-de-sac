from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Assurez-vous que cette ligne est là
from django.conf.urls.static import static # Assurez-vous que cette ligne est là

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boutique.urls')),
]

# Gérer les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)