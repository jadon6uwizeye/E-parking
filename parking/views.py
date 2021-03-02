from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Block,ParkingSlip,Location,ParkingSlot,Reservation,Profile
from .forms import blockForm,ParkingSlotForm,ProfileForm,ParkingSlipForm,MyObjectReservation
import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, mixins
from .serializer import RegisterSerializer, UserSerializer
import jwt

def index(request):
    return render(request,'index.html')

def signup(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':

            form = SignUpForm(request.POST)


            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('login')
            else:
                form = SignUpForm()
                return render(request, 'registration/registration_form.html', {'form': SignUpForm})
   

def login(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,username)
                return redirect('index')
            else:
                messages.info(request,'Username or Password is incorrect')
        context={}
        
        return render(request,'registration/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    return render(request,'user_profile.html',{"profile":profile})

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


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

#Login API
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RESPONSE
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LocationList(APIView):
    def get(self,request,format=None):
        all_locations = Location.objects.all()
        serializers = LocationSerializer(all_locations,many=True)
        permission_classes = (IsAuthenticated,)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = LocationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockList(APIView):
    def get(self,request,format=None):
        all_blocks = Block.objects.all()
        serializers = BlockSerializer(all_blocks,many=True)
        permission_classes = (IsAuthenticated,)
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
        permission_classes = (IsAuthenticated,)
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
        permission_classes = (IsAuthenticated,)
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
        permission_classes = (IsAuthenticated,)
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
        permission_classes = (IsAuthenticated,)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SlipSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)