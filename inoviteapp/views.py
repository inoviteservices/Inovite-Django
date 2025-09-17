from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User

import random
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.core.mail import send_mail

#for mail (contact us)
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'about-us.html')

def internship(request):
    return render(request,'internship.html')

def tech(request):
    return render(request,'tech.html')

def nontech(request):
    return render(request,'nontech.html')

def blog(request):
    return render(request,'blog.html')