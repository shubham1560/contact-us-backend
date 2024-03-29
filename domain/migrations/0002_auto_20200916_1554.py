# Generated by Django 3.1 on 2020-09-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_path',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='domain',
            name='type',
            field=models.CharField(choices=[('sp', 'Service Provider'), ('vr', 'Vendor'), ('cr', 'Customer')], default='cr', max_length=2),
        ),
    ]
