from django.contrib import admin
from django.urls import path, include  # Asigură-te că include este importat
from django.conf import settings  # Importă setările
from django.conf.urls.static import static  # Importă static pentru fișiere media


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Asigurați-vă că includeți URL-urile din accounts
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


