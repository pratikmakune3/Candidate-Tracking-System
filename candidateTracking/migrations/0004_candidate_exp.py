# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-18 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidateTracking', '0003_candidate_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='exp',
            field=models.IntegerField(null=True),
        ),
    ]
