from django.db import models

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
    Intersection_ID = models.ManyToManyField(Intersection)


class Driver(models.Model):
    National_ID = models.CharField(max_length=20, primary_key=True)
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Username = models.CharField(max_length=25)
    Encrypted_Password = models.CharField(max_length=15)


class EmergencyVehicle(models.Model):
    Car_ID = models.CharField(max_length=10, primary_key=True)
    Type = models.CharField(max_length=20)


class Use(models.Model):
    unique_together = ('National_ID', 'Car_ID')
    National_ID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Car_ID = models.ForeignKey(EmergencyVehicle, on_delete=models.CASCADE)
    Date = models.DateTimeField

