from django.shortcuts import render, redirect
from django.db.models import Q  
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser , Hostel_Details , HostelRoomDetails,Applicant_details


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
        room_numbers = HostelRoomDetails.objects.filter(hostel_name=hostel_name).values_list('room_no', flat=True)
        print(hostel_name)
    else:
        
        return redirect('login')
    context = {'hostel_name': hostel_name, 'user': user,'room_numbers': room_numbers}
    return render(request, 'hostel/dashboard.html', context)
    
def transactions(request, user):
    return render(request, 'hostel/view_transaction.html', {'user': user})

def fee_payment(request, user):
    return render(request, 'hostel/fee_payment.html', {'user': user})


def students_details(request, user):
    applicants = Applicant_details.objects.all()
    context = {'applicants': applicants , 'user': user}
    return render(request, 'hostel/student_details.html', context )



@csrf_exempt
def add_student(request,user):
    logged_in_user = user
    print(logged_in_user)
    hostel_details = Hostel_Details.objects.filter(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user)).first()
    
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('applicant_name')
        applicant_no = request.POST.get('application_no')
        program = request.POST.get('programme')
        year_of_admission = request.POST.get('year_of_admission')
        roll_no = request.POST.get('roll_no')
        joining_date = request.POST.get('joining_date')
        leaving_date = request.POST.get('leaving_date')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        fathers_name = request.POST.get('father_name')
        mothers_name = request.POST.get('mother_name')
        parent_phone_no = request.POST.get('parent_phone_no')
        parent_email = request.POST.get('parent_email')
        address = request.POST.get('address')
        localguardian_name = request.POST.get('localguardian_name')
        localguardian_mobile_no = request.POST.get('localguardian_mobile_no')
        deposit_amount = request.POST.get('deposit_amount', 0)
        room_no = request.POST.get('room_number')
        bed_no = request.POST.get('bed_number')
        total_fees = request.POST.get('total_fees', 0)
        fees_paid = request.POST.get('fees_paid', 0)
        fees_remaining = request.POST.get('fees_remaining', 0)
        
        print(room_no, bed_no)
        if hostel_details:
            hostel_name = hostel_details.hostel_name
        
        if room_no is not None and bed_no is not None:
            bed_num = room_no + bed_no
            print(room_no, bed_no)
            print (bed_num)
        else:
            bed_num = None
        
        # Create a new Applicant_details instance and save to the database
        new_applicant = Applicant_details(
            name=name,
            applicant_no=applicant_no,
            program=program,
            year_of_admission=year_of_admission,
            roll_no=roll_no,
            joining_date=joining_date,
            leaving_date=leaving_date,
            mobile_no=mobile_no,
            email_id=email,
            fathers_name=fathers_name,
            mothers_name=mothers_name,
            phone_no_of_parents=parent_phone_no,
            email_of_parents=parent_email,
            address_of_parents=address,
            local_guardian_name=localguardian_name,
            local_guardian_mobile_no=localguardian_mobile_no,
            deposit_amount=deposit_amount,
            hostel_name = hostel_name,
            user_registered = logged_in_user,
            room_no=room_no,
            bed_no=bed_num,
            total_fees=total_fees,
            fees_paid=fees_paid,
            fees_remaining=fees_remaining,
        )
        new_applicant.save()
        context = {'hostel_name': hostel_name, 'user': user}
        return render(request, 'hostel/dashboard.html', context)
        # return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})
