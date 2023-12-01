from django.shortcuts import render

# Create your views here.

def dashboard(request):

    # if guesthouse admin logged in this return will perform
        # return render(request, 'guesthouse/dashboard.html')
    # else if it is guest user then this will render
    return render(request, 'guesthouse/guest_user_dashboard.html')

# For Guest User to view their bookings
def my_bookings(request):
    return render(request, 'guesthouse/guest_user_my_bookings.html')

def my_accounts(request):
    return render(request, 'guesthouse/guest_user_my_accounts.html')


