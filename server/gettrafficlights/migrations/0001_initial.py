# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-24 13:09
from __future__ import unicode_literals

import database_functions
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
            name='CentralNode',
            fields=[
                ('CentralNode_ID', models.CharField(default=database_functions.centralnode_number, max_length=10, primary_key=True, serialize=False)),
                ('CentralNode_IP', models.CharField(default=b'0', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('National_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_driver', 'Can login as driver'),),
            },
        ),
        migrations.CreateModel(
            name='EmergencyVehicle',
            fields=[
                ('Car_ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Priority', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Intersection',
            fields=[
                ('Intersection_ID', models.CharField(default=database_functions.intersection_number, max_length=10, primary_key=True, serialize=False)),
                ('Intersection_Number_Central_Node', models.CharField(max_length=10)),
                ('CentralNode_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gettrafficlights.CentralNode')),
            ],
        ),
        migrations.CreateModel(
            name='IntersectionsStreets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Intersection_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gettrafficlights.Intersection')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('Street_ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Start_Longitude', models.FloatField(max_length=25)),
                ('Start_Latitude', models.FloatField(max_length=25)),
                ('End_Longitude', models.FloatField(max_length=25)),
                ('End_Latitude', models.FloatField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficLight',
            fields=[
                ('TL_ID', models.CharField(default=database_functions.trafficlights_number, max_length=10, primary_key=True, serialize=False)),
                ('Longitude', models.FloatField(max_length=25)),
                ('Latitude', models.FloatField(max_length=25)),
                ('Direction', models.CharField(max_length=2)),
                ('Intersection_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gettrafficlights.Intersection')),
            ],
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gettrafficlights.EmergencyVehicle')),
                ('National_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gettrafficlights.Driver')),
            ],
        ),
        migrations.AddField(
            model_name='intersectionsstreets',
            name='Street_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gettrafficlights.Street'),
        ),
    ]
