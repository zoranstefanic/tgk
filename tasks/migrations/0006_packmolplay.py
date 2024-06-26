# Generated by Django 3.1.4 on 2023-04-18 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_auto_20160924_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackmolPlay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chebi', models.CharField(max_length=30)),
                ('cell', models.CharField(max_length=30)),
                ('mol', models.TextField()),
                ('score', models.FloatField(null=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='packmols', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
