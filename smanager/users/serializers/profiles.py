"""Profile serializer. """

# Django REST Framework
from rest_framework import serializers

# Models
from smanager.users.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    """Profile Model Serializer. """

    class Meta:
        """Meta Class."""
        model = Profile

        fields = (
                'picture',
                'adress',
                'machines_taken',
                'service_taken',
                )

        read_only_fields = (
              'machines_taken',
              'service_taken',
              )
