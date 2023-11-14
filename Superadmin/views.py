from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import  Hostel_DetailsForm
from Hostel.models import Hostel_Details
# Create your views here.

def dashboard(request):
    form = Hostel_DetailsForm()
    hostel_datails = Hostel_Details.objects.all()
    context = {
        'form': form,
        'hostel_datails': hostel_datails
    }
    return render(request, 'dashboard.html',context)    

    # return HttpResponse("hello")


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return request('login')
            
    return render(request,'login.html')