from django.contrib import admin
from .models import DomainPreference


# Register your models here.


class DomainPreferenceAdmin(admin.ModelAdmin):
    model = DomainPreference
    list_display = ['id', 'user', 'domain', 'device_type']
    exclude = ('sys_created_on', 'sys_created_by', 'sys_updated_on', 'sys_updated_by',)
    ordering = ['-sys_created_on']


admin.site.register(DomainPreference, DomainPreferenceAdmin)
