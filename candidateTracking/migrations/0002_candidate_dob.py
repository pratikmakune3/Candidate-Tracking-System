# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-17 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidateTracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='dob',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
