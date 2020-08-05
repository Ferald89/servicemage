"""Services URLs. """

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import services as services_views

router = DefaultRouter()
router.register(
            r'machines/(?P<serial_number>[a-zA-Z0-p_-]+)/services',
            services_views.ServiceViewSet,
            basename='services'
            )

urlpatterns = [
            path('', include(router.urls))
            ]
