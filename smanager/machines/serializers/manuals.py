""""Manual serializer."""

# Django REST FrameWork
from rest_framework import serializers

# Model
from smanager.machines.models import Manual


class ManualModelSerializer(serializers.ModelSerializer):
    """Serializer model serializer."""

    class Meta:
        """MEta class."""
        model = Manual
        fields = (
            'id',
            'name',
            'file',
        )

    def validate(self, data):
        return data
