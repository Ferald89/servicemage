"""Project permissions classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsMachineAdmin(BasePermission):
    """Allow acess. only to project admins."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)
