# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 00:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evil_dog_image', '0006_paintings_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='charitydesign',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 18, 0, 36, 29, 572286, tzinfo=utc), verbose_name='Uploaded at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='graphicdesign',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 9, 18, 0, 36, 50, 928176, tzinfo=utc), verbose_name='Uploaded at'),
            preserve_default=False,
        ),
    ]
