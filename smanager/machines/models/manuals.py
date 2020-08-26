"""Manuals model. """

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Manual(SManageModel):
    """Manual model
    A manual when stored statics file of machine like manuals
    """
    used_in = models.ForeignKey(
                                'machines.Machine',
                                on_delete=models.CASCADE,
                                verbose_name='Máquina del manual'
                                )
    name = models.CharField('Nombre del Manual', max_length=140)
    file = models.FileField('Pdf Manual', null=False)
