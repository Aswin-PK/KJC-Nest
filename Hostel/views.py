from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from .models import CustomUser


# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     else:
#         if request.method == 'POST':
#             email = request.POST.get('Email')
#             password = request.POST.get('password')
#             print(email,password)
#             # Authenticate the user
#             authenticated_user = CustomUser.objects.get(email=email)
#             print("authenticated")
#             passw = authenticated_user.password
#             print(authenticated_user)
#             if authenticated_user is not None:
#                 if passw == password:
#                     print("User value got")
#                     # Fetch user details
#                     try:
#                         authenticated_user = CustomUser.objects.get(email=email)
#                         usert = authenticated_user.usertype
#                         print(usert)
#                         if usert == "Hostel_admin":
#                             return redirect('hostel/dashboard')
#                         elif usert == "Guest_Admin":
#                             return redirect('guesthouse/dashboard', {'data': authenticated_user})
#                         else:
#                             return redirect('/')
                            
#                     except CustomUser.DoesNotExist:
#                         usert = None
#                     # return redirect('dashboard')
#                     return redirect('/')
#                 else:
#                     messages.error(request, 'Invalid username or password')
#             else:
#                 print("If is not working")
#                 # Authentication failed, add an error message
#                 messages.error(request, 'Invalid username or password')
#                 # Return a response for failed authentication
#                 return render(request, 'login.html')
#         # Render the login page for GET requests
#         return render(request, 'login.html')


def dashboard(request):
    return render(request, 'hostel/dashboard.html')
    # return HttpResponse("hello")

def transactions(request):
    return render(request, 'hostel/view_transaction.html')

def fee_payment(request):
    return render(request, 'hostel/fee_payment.html')