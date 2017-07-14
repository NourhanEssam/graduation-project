# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Location(models.Model):
    Key = models.CharField(max_length=200, primary_key=True)
    lon = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    err = models.CharField(max_length=20)

    def __str__(self):
        return 'Key: ' + self.Key + ' - latitude: ' + self.lat + ' - longitude: ' + self.lon + ' - error ' + self.err
