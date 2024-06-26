# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-04 18:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task1Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now=True)),
                ('right', models.PositiveIntegerField(verbose_name='Number of right answers')),
                ('wrong', models.PositiveIntegerField(verbose_name='Number of wrong answers')),
                ('end', models.DateTimeField(blank=True, editable=False, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='plays', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
