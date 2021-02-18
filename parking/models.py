from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# Create your models here.
CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
)

class Location(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class ParkingLot(models.Model):
    number_of_blocks = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    is_reentry_allowed = models.CharField(max_length=1,choices=CHOICES )


class Block(models.Model):
    lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    block_code = models.CharField(max_length=3)
    is_block_full = models.CharField(max_length=1, choices=CHOICES)
    is_accessible = models.CharField(max_length=1)
    number_of_slots = models.PositiveIntegerField()



class ParkingSlot(models.Model):
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    slot_number = models.PositiveIntegerField()
    is_slot_available = models.CharField(max_length=1,choices=CHOICES)


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(default='No email')
    phone_No = models.CharField(max_length=10)
    plate_No = models.CharField(max_length=10)

  
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_plate(cls,id, plate_No):
        update_profile = cls.objects.filter(id = id).update(plate_No = plate_No)
        return update_profile

    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains=user).all()

class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plate_No = models.ForeignKey(Profile, on_delete=models.CASCADE)
    booking_date = models.DateField()
    Entry_time = models.TimeField(auto_now=True, auto_now_add=False)
    Exit_time = models.TimeField(auto_now=False, auto_now_add=False)
    duration_in_minutes = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    parking_slot_id = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)

    
    def save_reservation(self):
        self.save()

    def delete_reservation(self):
        self.delete()

class ParkingSlip(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slot_reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    entry_time = models.TimeField()
    exit_time = models.TimeField()
