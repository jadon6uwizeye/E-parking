from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('username','email','phone_No','plate_No')
    search_fields = ('username', 'plate_No')

class LocationAdmin(admin.ModelAdmin):
    list_display= ('name','latitude','longitude')
    search_fields = ('name')

class ReservationAdmin(admin.ModelAdmin):
    list_display= ('booking_date','user_id','plate_No','location','parking_slot_id')
    search_fields = ('user_id')

class SlipAdmin(admin.ModelAdmin):
    list_display= ('user_id','slot_reservation_id','entry_time','exit_time')
    search_fields = ('user_id')

admin.site.register(Location,LocationAdmin)
admin.site.register(Block)
admin.site.register(ParkingSlot)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(ParkingSlip,SlipAdmin)