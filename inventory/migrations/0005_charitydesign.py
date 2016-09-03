# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-02 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_graphicdesign'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharityDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('amount', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
