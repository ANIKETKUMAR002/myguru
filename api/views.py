from django.shortcuts import render, redirect
from django.contrib.auth.models import User  #for user model defult
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q   #Q is a native Django task queue
from django.contrib.auth.decorators import login_required

# Create your views here.
def api_view(request):
    return render(request,'myguru-home.html')

def login_view(request):
    return render(request,'login.html')

def signup_view(request):
    return render(request,'signup.html')

def exam_list_view(request):
    return render(request,'exam-list.html')

def test_view(request):
    return render(request,'guru-expert-videos.html')

def innerpage_view(request):
    return render(request,'innerpage.html')

def happiness_well_being_view(request):
    return render(request,'happiness-well-being.html')



