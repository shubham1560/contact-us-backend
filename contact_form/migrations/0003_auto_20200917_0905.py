# Generated by Django 3.1 on 2020-09-17 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_domain_api_key'),
        ('contact_form', '0002_contactform_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='domain.domain'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='domain_path',
            field=models.CharField(default='/', max_length=256),
        ),
    ]
