# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
