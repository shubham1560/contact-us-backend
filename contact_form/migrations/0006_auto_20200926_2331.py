# Generated by Django 3.1 on 2020-09-26 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0005_contactform_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='sys_created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contactform',
            name='sys_updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
