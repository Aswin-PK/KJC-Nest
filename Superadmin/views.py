from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import  Hostel_DetailsForm
from django.http import JsonResponse
from Hostel.models import CustomUser

def adminsave(request):
    if request.method == 'POST':
        admin_name = request.POST.get('adminName')
        admin_email = request.POST.get('adminEmail')
        phone = request.POST.get('phone')
        hostel_type = request.POST.get('hostelType')
        print(admin_email,admin_name)
        if hostel_type == "Hostel":
            usert = "Hostel Admin"
        elif hostel_type == "Guest House":
            usert = "Guest Admin"
        else:
            usert = None
        CustomUser.objects.create(email=admin_email,username=admin_name,password=admin_email,mobile=phone,usertype = usert)

        # Respond with a success message
        return JsonResponse({'message': 'Admin added successfully'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'})
# Create your views here.

def dashboard(request):
    form = Hostel_DetailsForm()
    context = {
        'form': form
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