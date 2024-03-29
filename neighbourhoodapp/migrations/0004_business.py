# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 07:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbourhoodapp', '0003_auto_20181018_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30, null=True)),
                ('business_email_address', models.CharField(max_length=200, null=True)),
                ('neighbourhood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhoodapp.Neighbourhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
