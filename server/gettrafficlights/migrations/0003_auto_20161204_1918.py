# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gettrafficlights', '0002_auto_20161204_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contains',
            name='Intersection_ID',
        ),
        migrations.RemoveField(
            model_name='contains',
            name='Street_ID',
        ),
        migrations.AddField(
            model_name='street',
            name='Intersection_ID',
            field=models.ManyToManyField(to='gettrafficlights.Intersection'),
        ),
        migrations.DeleteModel(
            name='Contains',
        ),
    ]