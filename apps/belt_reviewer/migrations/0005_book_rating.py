# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-22 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_reviewer', '0004_auto_20170922_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]
