from django.db import models
from .business_rules import after_insert, before_insert

# Create your models here.

DOMAIN_TYPE = (
        ('sp', 'Service Provider'),
        ('vr', 'Vendor'),
        ('cr', 'Customer'),
    )


class Domain(models.Model):
    active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    primary = models.BooleanField(default=False, blank=True, null=True)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    domain_code = models.CharField(max_length=6)
    domain_path = models.CharField(max_length=256, unique=True)
    type = models.CharField(choices=DOMAIN_TYPE, max_length=2, default="cr")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        before_insert(self)
        super().save(*args, **kwargs)
        after_insert(self)

    def delete(self, using=None, keep_parents=False):
        print("deleting the mofo mofo!")
        # breakpoint()
        super(Domain, self).delete()
        
    # def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
    #     breakpoint()
        # super()._do_update(base_qs, using, pk_val, values, update_fields, forced_update)
