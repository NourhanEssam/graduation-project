from django.contrib import admin

# username: yasminemohammad
# password: mAyEsTro0o

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import TrafficLight, Intersection, IntersectionsStreets, Street, Driver, EmergencyVehicle, CentralNode
admin.site.register(TrafficLight)

admin.site.register(Intersection)

admin.site.register(IntersectionsStreets)

admin.site.register(Street)

admin.site.register(Driver)

admin.site.register(EmergencyVehicle)

admin.site.register(CentralNode)