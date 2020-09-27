from django.contrib import admin
from .models import ContactForm

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    model = ContactForm
    list_display = ['id', 'email', 'domain', 'read', 'important', 'starred']


admin.site.register(ContactForm, ContactFormAdmin)