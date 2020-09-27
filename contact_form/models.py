from django.db import models
from django_countries.fields import CountryField
# Create your models here.
from domain.models import Domain
from .business_rules import before_insert, after_insert


class ContactForm(models.Model):
    read = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(null=True, blank=True, blank_label='(select country)')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    anything_else = models.TextField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True, default=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True, blank=True)
    domain_path = models.CharField(max_length=256, default='/')
    sys_created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sys_updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.email or '' + ' ' + self.subject or ''

    def save(self, *args, **kwargs):
        before_insert(self)
        super().save(*args, **kwargs)
        after_insert(self)