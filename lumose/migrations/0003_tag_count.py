# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumose', '0002_photo_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
