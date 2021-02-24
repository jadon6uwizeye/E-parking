from rest_framework import serializers
from .models import Location,Block,ParkingSlot,Profile,Reservation,ParkingSlip

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'latitude','longitude','building','building_photo')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('location','block_photo','block_code','is_block_full','is_accessible', 'number_of_slots')

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ('block_id', 'slot_number','is_slot_available','slot_photo')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email','phone_No','plate_No')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('booking_date', 'user_id','plate_No','Entry_time','Exit_time','duration_in_minutes','location','parking_slot_id')

class SlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlip
        fields = ('user_id', 'slot_reservation_id','entry_time','exit_time')