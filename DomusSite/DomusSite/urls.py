from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('main', include('main.urls')),
    path('login', include('login.urls')),
    path('account', include('account.urls')),
    path('market', include('usersmain.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
