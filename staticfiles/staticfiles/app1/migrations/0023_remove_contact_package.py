# Generated by Django 5.1.3 on 2025-02-11 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_contact_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='package',
        ),
    ]
