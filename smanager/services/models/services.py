"""Services model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Service(SManageModel):
    """Services models"""

    name = models.CharField('services name', max_length=140)

    about = models.TextField(blank=True)
