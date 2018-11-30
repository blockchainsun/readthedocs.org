# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import readthedocs.integrations.utils


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0003_add_missing_model_change_migrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='integration',
            name='secret',
            field=models.CharField(blank=True, default=readthedocs.integrations.utils.get_secret, max_length=255),
        ),
    ]
