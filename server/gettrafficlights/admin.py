from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import TrafficLight
admin.site.register(TrafficLight)

from .models import Intersection
admin.site.register(Intersection)

from .models import Street
admin.site.register(Street)

from .models import Driver
admin.site.register(Driver)

from .models import EmergencyVehicle
admin.site.register(EmergencyVehicle)