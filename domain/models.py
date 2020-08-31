from django.db import models

# Create your models here.

DOMAIN_TYPE = (
        ('sp', 'Service Provide'),
        ('vr', 'Vendor'),
        ('cr', 'Customer'),
    )


class Domain(models.Model):
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    primary = models.BooleanField(default=False, blank=True, null=True)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    domain_code = models.CharField(max_length=6)
    domain_path = models.CharField(max_length=256)
    type = models.CharField(choices=DOMAIN_TYPE, max_length=2, default="cr")
