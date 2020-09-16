from django.contrib import admin
from .models import ContactForm

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    model = ContactForm


admin.site.register(ContactForm, ContactFormAdmin)