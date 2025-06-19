from django.contrib import admin
from django.urls import path, include
from accounts.views import dashboard_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard_view),  # Set dashboard as homepage
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('startups/', include('startups.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)