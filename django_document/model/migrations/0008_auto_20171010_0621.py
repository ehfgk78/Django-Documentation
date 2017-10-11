# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_twitteruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='model.Topping'),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_twitteruser_friends_+', to='model.TwitterUser'),
        ),
    ]