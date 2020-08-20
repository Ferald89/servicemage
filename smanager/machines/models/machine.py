"""machines model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Machine(SManageModel):
    """Machine model."""

    name = models.CharField('Nombre De Máquina', max_length=140)
    serial_number = models.SlugField('Número de serie', unique=True, max_length=140)
    model = models.CharField('Modelo', max_length=140)
    about = models.CharField('Descripción De Máquina', max_length=255)
    picture = models.ImageField('Imagen', upload_to='machine/picture', blank=True, null=True)
    next_service = models.DateTimeField('Proximo servicio')

    owner = models.ForeignKey(
                        "users.User",
                        on_delete=models.CASCADE,
                        null=False,
                        verbose_name='Propietario'
                )

    def __str__(self):
        """Return Machine name."""
        return self.name
