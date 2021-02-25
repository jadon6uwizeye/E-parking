from rest_framework import serializers
from .models import Location,Block,ParkingSlot,Profile,Reservation,ParkingSlip
from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'latitude','longitude','location_pic')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('block_code','block_photo','location','is_block_full','is_accessible', 'number_of_slots')

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