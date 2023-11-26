from django.shortcuts import render, redirect
from django.db.models import Q  
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from .models import CustomUser , Hostel_Details


def dashboard(request,user):
    logged_in_user = user
    print(logged_in_user)
    hostel_details = Hostel_Details.objects.filter(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user)).first()
    print(hostel_details)
    if hostel_details:
        hostel_name = hostel_details.hostel_name
    else:
        
        return redirect('login')
        messages("The Hostel is either not assigned or the password is wrong")
         # Check if the user is a hostel admin and get the hostel details
    return render(request, 'hostel/dashboard.html', {'hostel_name': hostel_name})


def transactions(request):
    return render(request, 'hostel/view_transaction.html')

def fee_payment(request):
    return render(request, 'hostel/fee_payment.html')