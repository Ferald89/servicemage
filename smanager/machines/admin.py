"""Machine models admin."""

# Django
from django.contrib import admin

# Models
from smanager.machines.models import Machine, Manual


# @admin.register(Machine)
# class MachineAdmin(admin.ModelAdmin):
#     """Machine model admin."""

#     list_display = ('owner',)
#     search_fields = ('owner__username', 'owner__email',)
#     # list_filter = ('service_taken',)


admin.site.register(Manual)
admin.site.register(Machine)
