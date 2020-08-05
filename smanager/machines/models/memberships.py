"""Membership model."""

# Django
from django.db import models

# Utilities
from smanager.utils.models import SManageModel


class Membership(SManageModel):
    """SManage model.
    A membership is the table  that holds the relationship between
    a user and a machine
    """

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    machine = models.ForeignKey("machines.Machine", on_delete=models.CASCADE)

    # Status
    is_active = models.BooleanField(
                        'active status',
                        default=True,
                        help_text='Only active user ar allowed to interact with the machine'
    )

    is_owner = models.BooleanField(
        'machine admin',
        default=False,
        help_text="Machine admin can see you detail"
        )

    def __str__(self):
        """Return username and machine."""
        return '@{} at #{}'.format(
                            self.user.username,
                            self.machine.serial_number
                            )
