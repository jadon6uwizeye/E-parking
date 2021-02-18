from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Block,ParkingLot,ParkingSlip,Location,ParkingSlot,Reservation
from .forms import blockForm,ParkingSlotForm,ProfileForm,ParkingSlipForm,ReservationForm

import datetime as dt
from django.contrib.auth.models import User

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



