"""User Models."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from smanager.utils.models import SManageModel


class User(SManageModel, AbstractUser):
    """User mode.
    Extend from django's Abstact User,Change the username field
    to email and add some extra fields
    """
    email = models.EmailField(
        'Email',
        unique=True,
        error_messages={
                        'unique': 'A USer with that email already exist.'
        }
    )

    phone_regex = RegexValidator(
         regex=r'\+?1?\d{9,15}$',
         message="Phone number must be entered in the format: +9999999. up to 15 digits allowed."
         )

    phone_number = models.CharField('Telefono', validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_admin = models.BooleanField(
        verbose_name='Es Administrador',
        default=False,
        help_text='Set to true when the user is a an admin'
    )

    def ___str__(self):
        return self.username

    def get_short_name(self):
        return self.username
