from django import forms
from .models import Block,Reservation,Profile,ParkingSlip,ParkingSlot
from location_field.forms.plain import PlainLocationField
from djreservation.views import ProductReservationView
 
class Address(forms.Form):
    city = forms.CharField()
    # location = PlainLocationField(based_fields=['city'],initial='-22.2876834,-49.1607606')

class blockForm(forms.ModelForm):
    class Meta:
        model=Block
        exclude=['block_code','number_of_slots']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','email','phone_No','plate_No']

class ParkingSlotForm(forms.ModelForm):
    class Meta:
        model=ParkingSlot
        exclude=['slot_number']

class MyObjectReservation(ProductReservationView):
    class Meta:
        model=Reservation
        exclude=['Entry_time','Exit_time','location']

class ParkingSlipForm(forms.ModelForm):
    class Meta:
        model=ParkingSlip
        exclude=['entry_time','exit_time']