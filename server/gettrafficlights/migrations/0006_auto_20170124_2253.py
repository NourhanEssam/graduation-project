# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-24 20:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gettrafficlights', '0005_auto_20170124_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'permissions': (('is_driver', 'Can login as driver'),)},
        ),
    ]