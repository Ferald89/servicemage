"""Profile model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Profile(SManageModel):
    """Profile model.
    A profile hold a user's public data like picture,
    an statics.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE, verbose_name='Usuario')

    adress = models.CharField('Dirección', max_length=255)

    picture = models.ImageField(
                'Imagen de Perfil',
                upload_to='users/picture/',
                blank=True,
                null=True
    )

    # stats
    machines_taken = models.PositiveIntegerField(default=0, verbose_name='Máquinas obtenidas')

    service_taken = models.PositiveIntegerField(default=0, verbose_name='Servicios tomados')

    def __str__(self):
        """Return user's"""
        return str(self.user)
