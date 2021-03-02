from django.contrib import admin
from .models import *
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display= ('name','latitude','longitude')
    search_fields = ('name',)
    list_per_page = 5

class BlockAdmin(admin.ModelAdmin):
    list_display= ('block_code','location','is_block_full','is_accessible','number_of_slots')
    search_fields = ('block_code',)
    list_per_page = 5

class SlotAdmin(admin.ModelAdmin):
    list_display= ('slot_number','is_slot_available','block_id')
    search_fields = ('block_id',)
    list_per_page = 5

class ProfileAdmin(admin.ModelAdmin):
    list_display= ('username','email','phone_No','plate_No')
    search_fields = ('username', 'plate_No',)
    list_per_page = 5

class ReservationAdmin(admin.ModelAdmin):
    list_display= ('booking_date','user_id','plate_No','location','parking_slot_id')
    search_fields = ('name',)
    list_per_page = 5

class SlipAdmin(admin.ModelAdmin):
    list_display= ('user_id','slot_reservation_id','entry_time','exit_time')
    search_fields = ('user_id',)
    list_per_page = 5

admin.site.register(Location,LocationAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(ParkingSlot,SlotAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(ParkingSlip,SlipAdmin)