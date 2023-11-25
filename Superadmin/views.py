from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import  Hostel_DetailsForm
from django.http import JsonResponse
from Hostel.models import CustomUser

def adminsave(request):
    if request.method == 'POST':
        admin_name = request.POST.get('adminName')
        admin_email = request.POST.get('adminEmail')
        phone = request.POST.get('phone')
        hostel_type = request.POST.get('hostelType')
        
        if not (admin_name and admin_email and phone and hostel_type):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        print(admin_email,admin_name)
        
        if hostel_type == "Hostel":
            usert = "Hostel_admin"
        elif hostel_type == "Guest House":
            usert = "Guest_admin"
        else:
            usert = None
            
        print(usert)
        user = CustomUser.objects.create(email=admin_email, username=admin_name,password=admin_email, mobile=phone, usertype=usert)
        user.save()
        # return render(request,'dashboard.html')
        messages.success(request, 'Data successfully saved!')
        return render(request,'dashboard.html')
        # Respond with a success message
# Respond with a success message
        # return JsonResponse({'message': 'Admin added successfully'}, status=201)
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
# Create your views here.

def dashboard(request):
   
    return render(request, 'dashboard.html')    

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


 
  
# def update_hostel(request, Hostel_ID):     
#     item = Hostel_Details.objects.get(Hostel_ID = Hostel_ID)    
#     if request.method == 'POST':        
#         form = Hostel_DetailsForm(request.POST, instance=item)       
#         if form.is_valid():           
#             form.save()  
#         else:
#          form = Hostel_DetailsForm(instance=item)
#     return render(request, 'dashboard.html', {'form': form, 'item': item})