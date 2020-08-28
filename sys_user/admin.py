from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SysUser


# Register your models here.

class SysUserAdmin(UserAdmin):
    model = SysUser


admin.site.register(SysUser, SysUserAdmin)