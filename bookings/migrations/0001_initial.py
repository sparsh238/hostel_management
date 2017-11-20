# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occupant', models.CharField(max_length=50, blank=True)),
                ('room_number', models.CharField(max_length=10)),
                ('roll_number', models.CharField(max_length=10, blank=True)),
                ('occupied', models.BooleanField(default=False)),
            ],
        ),
    ]
