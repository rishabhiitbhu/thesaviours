# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20160629_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
