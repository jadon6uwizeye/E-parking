from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Block,ParkingLot,ParkingSlip,Location,ParkingSlot,Reservation,Profile
from .forms import blockForm,ParkingSlotForm,ProfileForm,ParkingSlipForm,ReservationForm
import datetime as dt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *



# def index(request):
#     try:
#         if not request.user.is_authenticated:
#             return redirect('/accounts/login/')
#         current_user=request.user
#         profile =Profile.objects.get(username=current_user)
#     except ObjectDoesNotExist:
#         return redirect('create-profile')

#     return render(request,'index.html')
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})

# @login_required(login_url='/accounts/login/')
# def my_profile(request):
#     current_user=request.user
#     profile =Profile.objects.get(username=current_user)

#     return render(request,'user_profile.html',{"profile":profile})

# @login_required(login_url='/accounts/login')
# def reservation(request):
#     current_user=request.user
#     profile=Profile.objects.get(username=current_user)


# @login_required(login_url='/accounts/login/')
# def new_reservation(request):
#     current_user=request.user
#     profile =Profile.objects.get(username=current_user)

#     if request.method=="POST":
#         form =ReservationForm(request.POST,request.FILES)
#         if form.is_valid():
#             reservation = form.save(commit = False)
#             reservation.username = current_user
#             reservation.plate_no = reservation.plate_no
#             reservation.entry_time = reservation.entry_time
#             blogpost.exit_time = reservation.exit_time
#             blogpost.save()

#         return HttpResponseRedirect('/reservation')

#     else:
#         form = BlogPostForm()

#     return render(request,'reservation_form.html',{"form":form})


# @login_required(login_url='/accounts/login/')
# def create_profile(request):
#     current_user=request.user
#     if request.method=="POST":
#         form =ProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             profile = form.save(commit = False)
#             profile.username = current_user
#             profile.save()
#         return HttpResponseRedirect('/')

#     else:

#         form = ProfileForm()
#     return render(request,'profile_form.html',{"form":form})



# @login_required(login_url='/accounts/login/')
# def update_profile(request):
#     current_user=request.user
#     if request.method=="POST":
#         instance = Profile.objects.get(username=current_user)
#         form =ProfileForm(request.POST,request.FILES,instance=instance)
#         if form.is_valid():
#             profile = form.save(commit = False)
#             profile.username = current_user
#             profile.save()

#         return redirect('Index')

#     elif Profile.objects.get(username=current_user):
#         profile = Profile.objects.get(username=current_user)
#         form = ProfileForm(instance=profile)
#     else:
#         form = ProfileForm()

#     # return render(request,'update_profile.html',{"form":form})

 
class LocationList(APIView):
    def get(self,request,format=None):
        all_locations = Location.objects.all()
        serializers = LocationSerializer(all_locations,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = LocationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LotList(APIView):
    def get(self,request,format=None):
        all_lots = ParkingLot.objects.all()
        serializers = LotSerializer(all_lots,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = LotSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BlockList(APIView):
    def get(self,request,format=None):
        all_blocks = Block.objects.all()
        serializers = BlockSerializer(all_blocks,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = BlockSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SlotList(APIView):
    def get(self,request,format=None):
        all_slots = ParkingSlot.objects.all()
        serializers = SlotSerializer(all_slots,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SlotSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationList(APIView):
    def get(self,request,format=None):
        all_reservations = Reservation.objects.all()
        serializers = ReservationSerializer(all_reservations,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ReservationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SlipList(APIView):
    def get(self,request,format=None):
        all_slips = ParkingSlip.objects.all()
        serializers = SlipSerializer(all_slips,many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SlipSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)