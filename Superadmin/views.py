from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.http import JsonResponse
from Hostel.models import CustomUser, Hostel_Details,HostelRoomDetails
from django.contrib.auth.decorators import login_required, user_passes_test


def signupuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(username,email,password)
        # Basic validation, you may want to add more robust validation
        if username and email and password:
            user_profile = CustomUser(username=username, email=email, password=password,mobile='null',usertype='User')
            user_profile.save()
            return redirect('success')  # Redirect to a success page or another URL

    return render(request, 'signup.html')



def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('Email')
            password = request.POST.get('password')
            print(email,password)
            try:
                authenticated_user = CustomUser.objects.get(email=email)
                print("authenticated")
                passw = authenticated_user.password
                print(authenticated_user)
                if authenticated_user is not None:
                    if passw == password:
                        usert = authenticated_user.usertype
                        print(usert)
                        if usert == "Hostel_admin":
                            return redirect(f'hostel/{authenticated_user.username}')
                        elif usert == "Guest_Admin":
                            return redirect(f'guesthouse/{authenticated_user.username}')
                        elif usert == "User":
                            print("user part is working")
                            return redirect(f'/{authenticated_user.username}')
                        else:
                            return redirect(f'/{authenticated_user.username}')
                    else:
                        messages.error(request, 'Invalid username or password')
                else:
                    print("If is not working")
                    # Authentication failed, add an error message
                    messages.error(request, 'Invalid username or password')
                    # Return a response for failed authentication
                    return render(request, 'login.html')
            except:
                messages.error(request, 'Invalid username or password')
                print("If is not working")
        else:
            
        # Render the login page for GET requests
            return render(request, 'login.html')
        
    return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    return redirect('/')


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
        messages.success(request, 'Data saved successfully!')
        return redirect('/')
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
# Create your views here.






@login_required(login_url='login')
def dashboard(request):
    
    hadmin_usernames = CustomUser.objects.filter(usertype='Hostel_admin').values_list('username', flat=True)
    # warden name collected from hostel datails table
    hostel_warden_1 = Hostel_Details.objects.values_list('hostel_warden_1', flat=True).distinct()
    hostel_warden_2 = Hostel_Details.objects.values_list('hostel_warden_2', flat=True).distinct()
    # Combine all warden
    assigned_wardens = list(set(hostel_warden_1) | set(hostel_warden_2))
    # take the warden names except data from 'combined all warden'
    note_assigned_wardens = CustomUser.objects.exclude(username__in=assigned_wardens).values_list('username', flat=True)
    print("all warden details except",note_assigned_wardens)
    hostel_wardens = CustomUser.objects.filter(usertype='Hostel_admin').values_list('username', flat=True)
    print("the hostel warden details is",hostel_wardens)
    hostel_details = Hostel_Details.objects.all()
    warden_details = [name for name in hostel_wardens if name in note_assigned_wardens]
    context = {
        'admin_usernames': hadmin_usernames,
        'warden_details': warden_details,
        'hostel_details': hostel_details
    }
    return render(request, 'dashboard.html',context )    

 
  
def hostel_save(request):
    if request.method == 'POST':
        hostel_Name = request.POST.get('hostelname')
        hostel_admins = request.POST.getlist('admins')
        hostel_address = request.POST.get('hostel_address')
       
        if not(hostel_Name and len(hostel_admins) > 0  and hostel_address ):
            return JsonResponse({'error':'All fields are required '})
        if len(hostel_admins) > 2:
             return JsonResponse({'error':'Do not select more than 2 waden'})    
        else:
            hostel_data = {
                'hostel_name': hostel_Name,
                'hostel_warden_1': hostel_admins[0],
                'hostel_warden_2': hostel_admins[1] if len(hostel_admins) > 1 else None,
                'hostel_address': hostel_address
                }
            hostel_details = Hostel_Details.objects.create(**hostel_data) 
            print(hostel_details)
            if hostel_details:
                messages.success(request, 'Data saved successfully!')
                return redirect('/')
                #  return JsonResponse({'response': True})
            else:
                # If the form is not valid, return JsonResponse with error message
                return JsonResponse({'response': False, 'error': 'Form is not valid'})
    
                # return JsonResponse({'success': 'Data Saved'})        
    return render(request,'dashboard.html')

def signup(request):
    return render(request, 'signup.html')