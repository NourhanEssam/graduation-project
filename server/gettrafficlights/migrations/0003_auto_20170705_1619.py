# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gettrafficlights', '0002_auto_20170705_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centralnode',
            name='CentralNode_IP',
            field=models.CharField(default=b'0', max_length=15),
        ),
    ]
