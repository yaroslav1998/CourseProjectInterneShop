# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=1024)),
                ('password', models.CharField(max_length=1024)),
                ('role', models.CharField(max_length=1024)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=1024)),
                ('adress', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
