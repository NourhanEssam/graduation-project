from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Intersection(models.Model):
    Intersection_ID=models.CharField(max_length=4)

class TrafficLight( models.Model):
    TL_ID=models.CharField(max_length=5)
    Longitude=models.CharField(max_length=25)
    Latitude=models.CharField(max_length=25)
    Direction=models.CharField(max_length=2)
    Intersection_ID=models.ForeignKey(Intersection,on_delete=models.CASCADE)
class Street( models.Model):
    Street_ID=models.CharField(max_length=5)
    Start_Longitude=models.CharField(max_length=25)
    Start_Latitude=models.CharField(max_length=25)
    End_Longitude = models.CharField(max_length=25)
    End_Latitude = models.CharField(max_length=25)

class Driver( models.Model):
    National_ID=models.CharField(max_length=5)
    First_Name=models.CharField(max_length=250)
    Last_Name=models.CharField(max_length=250)
    Username=models.CharField(max_length=25)
    Encrypted_Password=models.CharField(max_length=25)

class EmergencyVehicle(models.Model):
    Car_ID=models.CharField(max_length=10)
    Type=models.CharField(max_length=20)

class Contains(models.Model):
    Intersection_ID=models.ForeignKey(Intersection, on_delete=models.CASCADE)
    Street_ID=models.ForeignKey(Street, on_delete=models.CASCADE)

class Use(models.Model):
    National_ID=models.ForeignKey(Driver, on_delete=models.CASCADE)
    Car_ID=models.ForeignKey(EmergencyVehicle, on_delete=models.CASCADE)
    Date=models.DateTimeField

