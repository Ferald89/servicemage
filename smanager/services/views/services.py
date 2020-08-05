""""Services views."""

# Django REST Frameworks
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from smanager.services.serializers import ServiceModelSerializer, CreateServiceSerializer

# Models
from smanager.machines.models import Machine


class ServiceViewSet(
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """Item view set."""

    def dispatch(self, request, *args, **kwargs):
        """Verify that the project exists. """
        serial_number = kwargs['serial_number']
        self.machine = get_object_or_404(Machine, serial_number=serial_number)
        return super(ServiceViewSet, self).dispatch(request, *args, **kwargs)

    def get_permissions(self):
        """Assign permission based on action"""
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_context(self):
        """Add machine to serializer context"""
        context = super(ServiceViewSet, self).get_serializer_context()
        context['machine'] = self.machine
        return context

    def get_serializer_class(self):
        """Return serializer based on action. """
        if self.action == 'create':
            return CreateServiceSerializer
        return ServiceModelSerializer

    def get_queryset(self):
        """Return active projec's item."""
        return self.machine.service_set.all()
