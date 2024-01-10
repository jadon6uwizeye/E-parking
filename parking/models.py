from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
)

class Location(models.Model):
    name = models.CharField(max_length=100,null=True)
    location_pic = models.ImageField(upload_to='building/',default='media/auca.jpeg')
    latitude = models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)],null=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)],null=True)

    # def __str__(self):
    #     if self.name==None:
    #         return "ERROR-CUSTOMER NAME IS NULL"
    #     return self.name


class Block(models.Model):
    block_code = models.CharField(max_length=3)
    block_photo = models.ImageField(upload_to='blocks/',default='media/defaultblock.jpeg')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    is_block_full = models.CharField(max_length=1, choices=CHOICES)
    is_accessible = models.CharField(max_length=1)
    number_of_slots = models.PositiveIntegerField()

    # def __str__(self):
    #     if self.block_code==None:
    #         return "ERROR-CUSTOMER NAME IS NULL"
    #     return self.block_code


class ParkingSlot(models.Model):
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE)
    slot_number = models.PositiveIntegerField()
    is_slot_available = models.CharField(max_length=1,choices=CHOICES)
    slot_photo = models.ImageField(upload_to='slots/',default='media/defaultslot.jpeg')

    # def __str__(self):
    #     if self.block_id==None:
    #         return "ERROR-CUSTOMER NAME IS NULL"
    #     return self.block_id


class Profile(models.Model):
    username= models.OneToOneField(User, on_delete=models.CASCADE)
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

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

class Reservation(models.Model):
    booking_date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id', null=True, blank=True)
    plate_No = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    Entry_time = models.TimeField(auto_now=False, auto_now_add=False)
    Exit_time = models.TimeField(auto_now=False, auto_now_add=False)
    duration_in_minutes = models.PositiveIntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    parking_slot_id = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE, null=True, blank=True)

    
    def save_reservation(self):
        self.save()

    def delete_reservation(self):
        self.delete()

class ParkingSlip(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slot_reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    entry_time = models.TimeField()
    exit_time = models.TimeField()

