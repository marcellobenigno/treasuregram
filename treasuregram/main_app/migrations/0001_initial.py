# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=255)),
            ],
        ),
    ]
