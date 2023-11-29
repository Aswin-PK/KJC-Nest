from django.shortcuts import render, redirect
from django.db.models import Q  
from django.contrib import messages
from django.http import JsonResponse
from .models import CustomUser , Hostel_Details , HostelRoomDetails


def hroomsave(request,user):
    print("hello", ">>>>",user)
    if request.method == 'POST':
        logged_in_user = user
        print(logged_in_user)
        hostel_details = Hostel_Details.objects.filter(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user)).first()
        if hostel_details:
            hostel_name = hostel_details.hostel_name
            print(hostel_name)
        roomnumber = request.POST.get('roomnumber')
        bedcount = int(request.POST.get('bedcount'))
        bed1price = request.POST.get('bed1price')
        bed2price = request.POST.get('bed2price')
        bed3price = request.POST.get('bed3price')
        bed4price = request.POST.get('bed4price')
        bathroomattached = request.POST.get('bathroomattached')
        
        print(">><<>><<>>",user,hostel_name, roomnumber)
        
        if not (roomnumber and bedcount and bed1price and bathroomattached):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        if bathroomattached == "on":
            bath = True
        else:
            bath = False
        print(hostel_name,roomnumber,bathroomattached,bath)
        hostel = HostelRoomDetails.objects.create(
                    hostel_name=hostel_name,
                    room_no=roomnumber,
                    no_of_beds=bedcount,
                    bed_no1_id=f"{roomnumber}B1",
                    bed_no1_price=bed1price,
                    bathroom_attached=bath
                )

                # Additional beds based on bedcount
        if bedcount >= 2:
            hostel.bed_no2_id = f"{roomnumber}B2"
            hostel.bed_no2_price = bed2price
        if bedcount >= 3:
            hostel.bed_no3_id = f"{roomnumber}B3"
            hostel.bed_no3_price = bed3price
        if bedcount == 4:
            hostel.bed_no4_id = f"{roomnumber}B4"
            hostel.bed_no4_price = bed4price

        hostel.save()

        messages.success(request, 'Data successfully saved!')
        return JsonResponse({'message': 'task done'}, status=200)
        
    else:
        return redirect('/')       
    # return JsonResponse({'error': 'Invalid HTTP method'}, status=405)



def dashboard(request,user):
    logged_in_user = user
    print(logged_in_user)
    hostel_details = Hostel_Details.objects.filter(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user)).first()
    if hostel_details:
        hostel_name = hostel_details.hostel_name
        print(hostel_name)
    else:
        
        return redirect('login')
    context = {'hostel_name': hostel_name, 'user': user}
    return render(request, 'hostel/dashboard.html', context)
    
def transactions(request, user):
    return render(request, 'hostel/view_transaction.html', {'user': user})

def fee_payment(request, user):
    return render(request, 'hostel/fee_payment.html', {'user': user})


def students_details(request, user):
    return render(request, 'hostel/student_details.html', {'user': user})

def settings(request, user):
    logged_in_user = user
    hostel_details = Hostel_Details.objects.get(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user))
    print(hostel_details)
    hostel_id = hostel_details.Hostel_ID
    if request.method == 'POST':
        hostel_name = request.POST.get('username')
        hostel_address = request.POST.get('hosteladdress')
        hostel_capacity = request.POST.get('hostelcapacity')
        mess_vendor = request.POST.get('vendorname')
        mess_fees = request.POST.get('mess-fee')

        hostel_data = {
                'hostel_name': hostel_name if hostel_name  else None,
                'hostel_address': hostel_address if hostel_address  else None,
                'hostel_capacity': hostel_capacity if hostel_capacity  else None,
                'mess_vendor': mess_vendor if mess_fees else None,
                # 'mess_fees': mess_fees if mess_fees else None
            }

        if hostel_id:
            # If an ID is provided, update the existing record
            Hostel_Details.objects.filter(Hostel_ID=hostel_id).update(**hostel_data)
        else:
            # If no ID is provided, create a new record
            Hostel_Details.objects.create(**hostel_data)
    return render(request, 'hostel/settings.html', {'user': user, 'hostel_details':hostel_details})


    
