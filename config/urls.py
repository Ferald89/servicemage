"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', include(('smanager.users.urls', 'users'), namespace='users')),
    path('', include(('smanager.machines.urls', 'machines'), namespace='machines')),
    path('', include(('smanager.services.urls', 'services'), namespace='services')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
