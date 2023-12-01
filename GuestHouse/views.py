from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .forms import GuestroomuserdetailsForm
from Hostel.models import CustomUser,Guestroom_Details,Guestroomuserdetails,GuestRoomcreation
# Create your views here.

def dashboard(request,user):
    logged_user = user
    print(logged_user)
    guest_details = Guestroom_Details.objects.filter(Q(Guestroom_admin_1=logged_user) | Q(Guestroom_admin_2=logged_user)).first()
    if guest_details:
        guestroom_name = guest_details.Guestroom_name
        userdetail = CustomUser.objects.get(username=logged_user)
        usertype=userdetail.usertype
    else:
        return redirect('login')
    context = {'guestroom_name': guestroom_name, 'user': user , 'usertype': usertype}
    return render(request, 'guesthouse/dashboard.html', context)

def groomsave(request,user):
    print("hello", ">>>>",user)
    if request.method == 'POST':
        logged_in_user = user
        guest_details = Guestroom_Details.objects.filter(Q(Guestroom_admin_1=logged_in_user) | Q(Guestroom_admin_2=logged_in_user)).first()
        if guest_details:
            Guestroom_name = guest_details.Guestroom_name
            print(Guestroom_name)
        roomnumber = request.POST.get('roomnumber')
        bedcount = int(request.POST.get('bedcount'))
        roomtype = request.POST.get('roomtype')
        includeAC = request.POST.get('includeAC')
        price = request.POST.get('price')
        
        print(">><<>><<>>",user,Guestroom_name, roomnumber)
        
        if not (roomnumber and bedcount and roomtype and price):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        if includeAC == "on":
            ac = True
        else:
            ac = False
        hostel = GuestRoomcreation.objects.create(
                    Guestroom_name=Guestroom_name,
                    Guestroom_room_number=roomnumber,
                    Guestroom_bed_count=bedcount,
                    Guestroom_room_type=roomtype,
                    Guestroom_with_AC=ac,
                    Guestroom_price=price
                )

            
        hostel.save()

        messages.success(request, 'Data successfully saved!')
        # redirect the page
        logged_user = user
        print(logged_user)
        guest_details = Guestroom_Details.objects.filter(Q(Guestroom_admin_1=logged_user) | Q(Guestroom_admin_2=logged_user)).first()
        if guest_details:
            guestroom_name = guest_details.Guestroom_name
        else:
            return redirect('login')
        context = {'guestroom_name': guestroom_name, 'user': user}
        return render(request, 'guesthouse/dashboard.html', context)
        
    else:
        # redirect the page
        logged_user = user
        print(logged_user)
        guest_details = Guestroom_Details.objects.filter(Q(Guestroom_admin_1=logged_user) | Q(Guestroom_admin_2=logged_user)).first()
        if guest_details:
            guestroom_name = guest_details.Guestroom_name
        else:
            return redirect('login')
        context = {'guestroom_name': guestroom_name, 'user': user}
        return render(request, 'guesthouse/dashboard.html', context)     
    # return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def userrequest(request,user):
    userdetail = CustomUser.objects.filter(username=user).first()
    usern = userdetail.email
    mob = userdetail.mobile
    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        visit_reason = request.POST.get('visit_reason')
        # form = GuestroomuserdetailsForm(request.POST, request.FILES)
        checkin = request.POST.get('check_in')
        checkout = request.POST.get('check_out') 
        print(checkin,checkout)
        price = request.POST.get('pay_amount') 
        roomtypes =request.POST.get('room_type')
        if roomtypes == 'A/C Single Bed':
            rtype = "AC_Single"
        elif roomtypes == 'Non A/C Single Bed':
            rtype = "Single"
        elif roomtypes == 'A/C Double Bed':
            rtype = "AC_Double"
        elif roomtypes == 'Non A/C Double Bed':
            rtype = "Double"
        elif roomtypes == 'Dormitory':
            rtype = "Dormetory"
            
        guestcreation = Guestroomuserdetails(
            name = uname,
            email_1 = email,
            mobile_no = phone,
            reason_of_visiting = visit_reason,
            date_of_checkin = checkin,
            date_of_checkout = checkout,
            final_amount = price,
            room_type=rtype
        )
        guestcreation.save()
        return render(request, 'guesthouse/guest_user_my_bookings.html', {'user': user})
    else:
        userdetail = CustomUser.objects.filter(username=user).first()
        context = { 'user': user , 'userdetail': userdetail}
        return render(request, 'guesthouse/guest_user_dashboard.html', context )
        

        


def user_dashboard(request,user):
    userdetail = CustomUser.objects.filter(username=user).first()
    context = { 'user': user , 'userdetail': userdetail}
    return render(request, 'guesthouse/guest_user_dashboard.html', context )

def my_bookings(request,user):
    return render(request, 'guesthouse/guest_user_my_bookings.html', {'user': user})

def my_accounts(request,user):
    return render(request, 'guesthouse/guest_user_my_accounts.html', {'user': user})

