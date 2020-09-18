from django.db import models
from .business_rules import after_insert, before_insert
from sys_user.models import SysUser
# Create your models here.


DEVICE_TYPE = (
    ('MLD', 'Mobile list display'),
    ('MFD', 'Mobile form display'),
    ('DLD', 'Desktop list display'),
    ('DFD', 'Desktop form display')
)


class DomainPreference(models.Model):
    device_type = models.CharField(choices=DEVICE_TYPE, default=2)
    domain = models.ForeignKey(Domain, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.BooleanField(default=True)
    last_name = models.BooleanField(default=True)
    country = models.BooleanField(default=True)
    name = models.BooleanField(default=True)
    email = models.BooleanField(default=True)
    subject = models.BooleanField(default=True)
    message = models.BooleanField(default=True)
    anything_else = models.BooleanField(default=True)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    sys_created_by = models.ForeignKey(SysUser, null=True, blank=True)
    sys_updated_by = models.ForeignKey(SysUser, null=True, blank=True)

    def save(self, *args, **kwargs):
        before_insert(self)
        super().save(*args, **kwargs)
        after_insert(self)