# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20160914_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task1play',
            options={'ordering': ['duration', '-wrong']},
        ),
    ]
