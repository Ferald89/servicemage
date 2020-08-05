"""Projects views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Permissions
from rest_framework.permissions import IsAuthenticated
from smanager.machines.permissions.machines import IsMachineAdmin

# Serializer
from smanager.machines.serializers import MachineModelSerializer
from smanager.users.serializers import UserModelSerializer

# Model
from smanager.machines.models import Machine, Membership
from smanager.users.models import User


class MachineViewSet(
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Project view set."""
    serializer_class = MachineModelSerializer
    lookup_field = 'serial_number'

    def get_queryset(self):
        """Restric list to public only"""
        queryset = Machine.objects.all()
        if self.action == 'list':
            # chenge to is public project
            return queryset
        return queryset

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsMachineAdmin)
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        """Assign machine admin"""
        machine = serializer.save()
        user = self.request.user
        profile = user.profile
        # import ipdb; ipdb.set_trace()
        Membership.objects.create(
            user=user,
            profile=profile,
            machine=machine,
            is_owner=True,
        )

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response"""
        response = super(MachineViewSet, self).retrieve(request, *args, **kwargs)
        user = User.objects.filter(
            id=response.data['owner'],
        )
        data = {
            'machine': response.data,
            'user': UserModelSerializer(user, many=True).data
        }
        response.data = data
        return response
