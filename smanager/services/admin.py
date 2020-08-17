"""Machine models admin."""

# Django
from django.contrib import admin

# Models
from smanager.services.models import Service


# @admin.register(Machine)
# class MachineAdmin(admin.ModelAdmin):
#     """Machine model admin."""

#     list_display = ('owner',)
#     search_fields = ('owner__username', 'owner__email',)
#     # list_filter = ('service_taken',)


admin.site.register(Service)
