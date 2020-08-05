"""machines model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Machine(SManageModel):
    """Machine model."""

    name = models.CharField('project name', max_length=140)
    serial_number = models.SlugField(unique=True, max_length=140)
    model = models.CharField('model', max_length=140)
    about = models.CharField('machine description', max_length=255)
    picture = models.ImageField(upload_to='machine/picture', blank=True, null=True)
    next_service = models.DateTimeField()

    owner = models.ForeignKey(
                        "users.User",
                        on_delete=models.CASCADE,
                        null=False
                )

    def __str__(self):
        """Return Machine name."""
        return self.name
