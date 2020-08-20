"""Services model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Service(SManageModel):
    """Services models"""

    owner_machine = models.ForeignKey(
                    "users.User",
                    on_delete=models.SET_NULL,
                    null=True,
                    verbose_name='Propietario de la Máquina'
    )

    order_in = models.ForeignKey(
                        "machines.Machine",
                        on_delete=models.SET_NULL,
                        null=True,
                        verbose_name='Servició ordenado en la máquina'
                    )
    name = models.CharField('Nombre Del Servicio', max_length=140)

    about = models.TextField('Acerca del service', blank=True)
    # status

    is_active = models.BooleanField(
                'El Servicio esta activo',
                default=True,
                help_text='used fot disabiling when the service was done'
    )

    taked_at = models.DateTimeField(verbose_name='Tomado en', null=True, blank=True)

    service_date = models.DateTimeField(verbose_name='Fecha del servicio')

    def __str__(self):
        """Return the service details."""
        return self.name
