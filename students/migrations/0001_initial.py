# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import students.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='hostel_fee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=30, choices=[(b'1st', b'1st'), (b'2nd', b'2nd'), (b'3rd', b'3rd'), (b'4th', b'4th')])),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mess_deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(max_length=30, choices=[(b'jan', b'January'), (b'feb', b'February'), (b'mar', b'March'), (b'may', b'April'), (b'apr', b'May'), (b'jun', b'June'), (b'jul', b'July'), (b'aug', b'August'), (b'sep', b'September'), (b'oct', b'October'), (b'nov', b'November'), (b'dec', b'December')])),
                ('bill', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('usn', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('fine_student', models.ManyToManyField(to='students.fine', blank=True)),
                ('hostel_fee_paid', models.ManyToManyField(to='students.hostel_fee', blank=True)),
                ('mess_bill_paid', models.ManyToManyField(to='students.mess_deposit', blank=True)),
            ],
            options={
                'ordering': ['usn'],
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'files/', verbose_name=b'xls', validators=[students.models.validate_file_extension])),
                ('name', models.CharField(default=b'tempfile', max_length=30)),
            ],
        ),
    ]
