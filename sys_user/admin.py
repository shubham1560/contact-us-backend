from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SysUser

# gettext_lazy = lazy(gettext, str)


# Register your models here.

class SysUserAdmin(UserAdmin):
    model = SysUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'domain', 'domain_path']
    # fieldsets = ('username', 'active')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'domain', 'domain_path'),
        }),
    )


admin.site.register(SysUser, SysUserAdmin)