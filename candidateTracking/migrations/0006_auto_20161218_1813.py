# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-18 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidateTracking', '0005_candidate_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='last_name',
            new_name='name',
        ),
    ]
