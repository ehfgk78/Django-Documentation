# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20171010_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
