# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20160908_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task1play',
            options={'ordering': ['-duration', '-wrong']},
        ),
        migrations.AddField(
            model_name='task1play',
            name='duration',
            field=models.DurationField(null=True),
        ),
    ]
