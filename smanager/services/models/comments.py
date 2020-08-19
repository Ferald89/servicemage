"""Comments model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Comment(SManageModel):
    """Comments models
    A Comment that can be used to add comments to services or machines
    """

    made_by = models.ForeignKey(
                "users.User",
                on_delete=models.SET_NULL,
                null=True
                )

    made_in = models.ForeignKey(
                "services.Service",
                on_delete=models.SET_NULL,
                null=True
    )

    is_active = models.BooleanField(
                'Es Activo',
                default=True,
                help_text='used fot disabiling when the service was done'
    )

    text = models.TextField(blank=True)
