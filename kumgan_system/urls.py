from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from kumgan_system import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kumgan.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
