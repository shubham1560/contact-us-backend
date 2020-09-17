from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class ContactForm(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(null=True, blank=True, blank_label='(select country)')
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    anything_else = models.TextField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.email or '' + ' ' + self.subject or ''
