"""Items serializers."""

# Django REST Frameworks
from rest_framework import serializers

# Serializers
from smanager.users.serializers import UserModelSerializer

# Models
from smanager.services.models import Service
from smanager.machines.models import Membership


class ServiceModelSerializer(serializers.ModelSerializer):
    """Service model serializer."""

    owner_machine = UserModelSerializer(read_only=True)
    order_in = serializers.StringRelatedField()

    class Meta:
        """Meta class."""

        model = Service
        fields = '__all__'
        read_only_fields = (
                    'owner_machine',
                    'order_in'
                    )


class CreateServiceSerializer(serializers.ModelSerializer):
    """Create Item Serializer."""

    owner_machine = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        """Meta class."""

        model = Service

        exclude = (
                'order_in',
                )

    def validate(self, data):
        """ Validate
        verify  that the person who orders the item is member
        and also the same user  making the request.
        """

        # if self.context['request'].user != data['owner_machine']:
        #     raise serializers.ValidationError('Serializer order on behalf of others are not allowed,')

        user = data['owner_machine']
        machine = self.context['machine']

        try:
            membership = Membership.objects.get(
                          user=user,
                          machine=machine
                          )
        except Membership.DoesNotExist:
            raise serializers.ValidationError('User is not an active member of the machine')

        self.context['membership'] = membership

        return data

    def create(self, data):
        """Create ride an update budget. """
        machine = self.context['machine']
        service = Service.objects.create(**data, order_in=machine)

        return service
