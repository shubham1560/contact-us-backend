from django.db import models
from .business_rules import after_insert_domain, before_insert_domain, \
    before_insert_domain_preference, \
    after_insert_domain_preference

# Create your models here.

DOMAIN_TYPE = (
        ('sp', 'Service Provider'),
        ('vr', 'Vendor'),
        ('cr', 'Customer'),
    )

DEVICE_TYPE = (
    ('MLD', 'Mobile list display'),
    ('MFD', 'Mobile form display'),
    ('DLD', 'Desktop list display'),
    ('DFD', 'Desktop form display')
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
    # default = models.BooleanField(default=False)
    api_key = models.CharField(max_length=32, null=True, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        before_insert_domain(self)
        super().save(*args, **kwargs)
        after_insert_domain(self)

    def delete(self, using=None, keep_parents=False):
        # print("deleting the mofo mofo!")
        # breakpoint()
        super(Domain, self).delete()

    # def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
    #     breakpoint()
        # super()._do_update(base_qs, using, pk_val, values, update_fields, forced_update)


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

    def save(self, *args, **kwargs):
        before_insert_domain_preference(self)
        super().save(*args, **kwargs)
        after_insert_domain_preference(self)