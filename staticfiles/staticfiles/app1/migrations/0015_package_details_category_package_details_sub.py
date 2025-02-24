# Generated by Django 5.1.3 on 2025-02-10 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_signinmodel_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='package_details_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='package_details_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1', models.CharField(max_length=100)),
                ('t2', models.CharField(max_length=100)),
                ('t3', models.CharField(max_length=100)),
                ('t4', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packagedetails', to='app1.package_details_category')),
            ],
        ),
    ]
