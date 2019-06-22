from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from vnl import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^location/', include('location.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
