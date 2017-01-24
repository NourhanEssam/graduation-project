from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Intersection(models.Model):
    Intersection_ID = models.CharField(max_length=10, primary_key=True)


class TrafficLight(models.Model):
    TL_ID = models.CharField(max_length=10, primary_key=True)
    Longitude = models.FloatField(max_length=25)
    Latitude = models.FloatField(max_length=25)
    Direction = models.CharField(max_length=2)
    Intersection_ID = models.ForeignKey(Intersection, on_delete=models.CASCADE)


class Street(models.Model):
    Street_ID = models.CharField(max_length=10, primary_key=True)
    Start_Longitude = models.FloatField(max_length=25)
    Start_Latitude = models.FloatField(max_length=25)
    End_Longitude = models.FloatField(max_length=25)
    End_Latitude = models.FloatField(max_length=25)


class IntersectionsStreets(models.Model):
    unique_together = ('Street_ID', 'Intersection_ID')
    Street_ID = models.ForeignKey(Street)
    Intersection_ID = models.ForeignKey(Intersection)


class Driver(models.Model):
    National_ID = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    class Meta:
        permissions = (
            ("is_driver", "Can login as driver"),
        )


class EmergencyVehicle(models.Model):
    Car_ID = models.CharField(max_length=10, primary_key=True)
    Priority = models.IntegerField(default=1)


class Use(models.Model):
    unique_together = ('National_ID', 'Car_ID')
    National_ID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Car_ID = models.ForeignKey(EmergencyVehicle, on_delete=models.CASCADE)
    Date = models.DateTimeField


