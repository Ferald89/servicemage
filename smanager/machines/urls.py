"""Machines URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# View
from .views import machines as machine_view

router = DefaultRouter()
router.register(r'machines', machine_view.MachineViewSet, basename='users')

urlpatterns = [
        path('', include(router.urls))
        ]
