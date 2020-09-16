from django.contrib import admin
from .models import Domain
# Register your models here.


class DomainAdmin(admin.ModelAdmin):
    model = Domain
    list_display = ['name', 'active', 'parent', 'domain_code', 'domain_path', 'type']
    fields = ['name', 'active', 'description', 'parent', 'type']
    ordering = ['-sys_created_on']


admin.site.register(Domain, DomainAdmin)