""""Machi serializer."""

# Django REST FrameWork
from rest_framework import serializers

# Model
from smanager.machines.models import Machine


class MachineModelSerializer(serializers.ModelSerializer):
    """Serializer model serializer."""

    class Meta:
        """MEta class."""
        model = Machine
        fields = (
            'name',
            'serial_number',
            'model',
            'about',
            'picture',
            'next_service',
            'owner',
        )

    def validate(self, data):
        return data
