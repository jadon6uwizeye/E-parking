from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Location)
admin.site.register(Block)
admin.site.register(ParkingSlot)
admin.site.register(Profile)
admin.site.register(Reservation)
admin.site.register(ParkingSlip)