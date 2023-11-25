from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import  Hostel_DetailsForm
from django.http import JsonResponse
from Hostel.models import CustomUser, Hostel_Details




def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('Email')
            password = request.POST.get('password')
            print(email,password)
            # Authenticate the user
            authenticated_user = CustomUser.objects.get(email=email)
            print("authenticated")
            passw = authenticated_user.password
            print(authenticated_user)
            if authenticated_user is not None:
                if passw == password:
                    print("User value got")
                    # Fetch user details
                    try:
                        authenticated_user = CustomUser.objects.get(email=email)
                        usert = authenticated_user.usertype
                        print(usert)
                        if usert == "Hostel_admin":
                            return redirect('hostel/')
                        elif usert == "Guest_Admin":
                            return redirect('guesthouse/', {'data': authenticated_user})
                        else:
                            return redirect('/')
                            
                    except CustomUser.DoesNotExist:
                        usert = None
                    # return redirect('dashboard')
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                print("If is not working")
                # Authentication failed, add an error message
                messages.error(request, 'Invalid username or password')
                # Return a response for failed authentication
                return render(request, 'login.html')
        # Render the login page for GET requests
        return render(request, 'login.html')


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
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
# Create your views here.



def hostelcreation(request):
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
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)




def dashboard(request):
    
    hadmin_usernames = CustomUser.objects.filter(usertype='Hostel_admin').values_list('username', flat=True)
    form = Hostel_DetailsForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard.html',{'context': context, 'admin_usernames': hadmin_usernames})    

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


 
  
def hostel_save(request):
    if request.method == 'POST':
        hostel_Name = request.POST.get('hostelname')
        hostel_admins = request.POST.getlist('admins')
        hostel_address = request.POST.get('hostel_address')
        print(hostel_admins)
        if not(hostel_Name and len(hostel_admins) > 0  and hostel_address ):
            return JsonResponse(
                {
                    'error':'All fields are required '
                }
            )
        hostel = Hostel_Details.objects.create(
            hostel_name =hostel_Name,
            hostel_warden_1=hostel_admins[0],
            hostel_warden_2=hostel_admins[1],
            hostel_address = hostel_address
            
        )
    return render(request,'dashboard.html')