from django.db import models

# Create your models here.


class Intersection(models.Model):
    Intersection_ID = models.CharField(max_length=10, primary_key=True)
    MAC = models.CharField(max_length=12, default='0')
    IP = models.CharField(max_length=8, default='0')

    def __str__(self):
        return self.Intersection_ID


class TrafficLight(models.Model):
    unique_together = ('TL_ID', 'Direction')
    TL_ID = models.CharField(max_length=10, primary_key=True)
    Longitude = models.FloatField(max_length=25)
    Latitude = models.FloatField(max_length=25)
    Direction = models.CharField(max_length=2)
    Intersection_ID = models.ForeignKey(Intersection, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.TL_ID) + ' - ' + str(self.Direction) + str(self.Intersection_ID)


class Street(models.Model):
    Street_ID = models.CharField(max_length=200, primary_key=True)
    Start_Longitude = models.FloatField(max_length=25)
    Start_Latitude = models.FloatField(max_length=25)
    End_Longitude = models.FloatField(max_length=25)
    End_Latitude = models.FloatField(max_length=25)

    def __str__(self):
        return self.Street_ID


class IntersectionsStreets(models.Model):
    unique_together = ('Street_ID', 'Intersection_ID')
    Street_ID = models.ForeignKey(Street)
    Intersection_ID = models.ForeignKey(Intersection)

    def __str__(self):
        return str(self.Intersection_ID) + ' - ' + str(self.Street_ID)


class Driver(models.Model):
    National_ID = models.CharField(max_length=20, primary_key=True)
    First_Name = models.CharField(max_length=250)
    Last_Name = models.CharField(max_length=250)
    Username = models.CharField(max_length=25)
    Encrypted_Password = models.CharField(max_length=25)

    def __str__(self):
        return self.Username


class EmergencyVehicle(models.Model):
    Car_ID = models.CharField(max_length=10, primary_key=True)
    Priority = models.IntegerField(default=1)

    def __str__(self):
        return self.Car_ID

class Use(models.Model):
    unique_together = ('National_ID', 'Car_ID')
    National_ID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Car_ID = models.ForeignKey(EmergencyVehicle, on_delete=models.CASCADE)
    Date = models.DateTimeField

    def __str__(self):
        return str(self.National_ID) + ' - ' + str(self.Car_ID)

