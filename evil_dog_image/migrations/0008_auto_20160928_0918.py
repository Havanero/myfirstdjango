# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evil_dog_image', '0007_auto_20160918_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='charitydesign',
            options={'ordering': ['-datetime']},
        ),
        migrations.AlterModelOptions(
            name='graphicdesign',
            options={'ordering': ['-datetime']},
        ),
        migrations.AlterModelOptions(
            name='paintings',
            options={'ordering': ['-datetime']},
        ),
    ]
