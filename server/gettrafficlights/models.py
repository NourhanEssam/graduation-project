from django.db import models
from django.contrib.auth.models import User


def Intersection_number():
    no = Intersection.objects.count()
    if no == None:
        return str(1)
    else:
        return str(no + 1)

def Central_Node_number():
    no = CentralNode.objects.count()
    if no == None:
        return str(1)
    else:
        return str(no + 1)

def TL_number():
    no = TrafficLight.objects.count()
    if no == None:
        return str(1)
    else:
        return str(no + 1)

# Create your models here.

class CentralNode(models.Model):
    CentralNode_ID = models.CharField(max_length=25, primary_key=True, default=Central_Node_number)
    CentralNode_IP = models.CharField(max_length=8, default='0')

    def __str__(self):
        return 'Central ID: ' + self.CentralNode_ID


class Intersection(models.Model):
    unique_together = ('Intersection_Number_Central_Node', 'CentralNode_ID')
    Intersection_ID = models.CharField(max_length=25, primary_key=True, default=Intersection_number)
    Intersection_Number_Central_Node = models.CharField(max_length=10)
    CentralNode_ID = models.ForeignKey(CentralNode, on_delete=models.CASCADE)
    #MAC = models.CharField(max_length=12, default='0')
    #IP = models.CharField(max_length=8, default='0')

    def __str__(self):
        return 'Intersection ID: ' + str(self.Intersection_ID) + ' - ' + str(self.CentralNode_ID)


class TrafficLight(models.Model):
    unique_together = ('Intersection_ID', 'Direction')
    TL_ID = models.CharField(max_length=25, primary_key=True, default=TL_number)
    Longitude = models.FloatField(max_length=25)
    Latitude = models.FloatField(max_length=25)
    Direction = models.CharField(max_length=2)
    Intersection_ID = models.ForeignKey(Intersection, on_delete=models.CASCADE)

    def __str__(self):
        return 'TL ID: ' + str(self.TL_ID) + ' - ' + 'Direction: ' + str(self.Direction) + ' - ' +  str(self.Intersection_ID)


class Street(models.Model):
    Street_ID = models.CharField(max_length=200, primary_key=True)
    Start_Longitude = models.FloatField(max_length=25)
    Start_Latitude = models.FloatField(max_length=25)
    End_Longitude = models.FloatField(max_length=25)
    End_Latitude = models.FloatField(max_length=25)

    def __str__(self):
        return 'Street ID: ' + self.Street_ID


class IntersectionsStreets(models.Model):
    unique_together = ('Street_ID', 'Intersection_ID')
    Street_ID = models.ForeignKey(Street)
    Intersection_ID = models.ForeignKey(Intersection)

    def __str__(self):
        return str(self.Intersection_ID) + ' - ' + str(self.Street_ID)


class Driver(models.Model):
    National_ID = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    class Meta:
        permissions = (
            ("is_driver", "Can login as driver"),
        )

    def __str__(self):
        return 'User ID: ' + self.user.username


class EmergencyVehicle(models.Model):
    Car_ID = models.CharField(max_length=10, primary_key=True)
    Priority = models.IntegerField(default=1)

    def __str__(self):
        return 'Car ID: ' + self.Car_ID


class Use(models.Model):
    unique_together = ('National_ID', 'Car_ID')
    National_ID = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Car_ID = models.ForeignKey(EmergencyVehicle, on_delete=models.CASCADE)
    Date = models.DateTimeField

    def __str__(self):
        return str(self.National_ID) + str(self.Car_ID)

