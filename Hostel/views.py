from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q  
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser , Hostel_Details , HostelRoomDetails,Applicant_details, FeesTransaction


def update_student(request, user):
    applicant_no = request.POST.get('application_no')
    if request.method == 'GET':
        # Retrieve the existing student data
        student = get_object_or_404(Applicant_details, applicant_no=applicant_no)
        applicants = Applicant_details.objects.all()
        logged_in_user = user
        print(logged_in_user)
        hostel_details = Hostel_Details.objects.filter(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user)).first()
        if hostel_details:
            hostel_name = hostel_details.hostel_name
            room_numbers = HostelRoomDetails.objects.filter(hostel_name=hostel_name).values_list('room_no', flat=True)
        
        # Render the form with existing data
        context = {
            'user': user,
            'student': student,
            'room_numbers': ['B1', 'B2', 'B3', 'B4'],
            'applicants': applicants ,  'room_numbers': room_numbers# Replace with your actual room numbers
        }
        return render(request, 'hostel/student_details.html', context )

    elif request.method == 'POST':
        # Process the form submission and update the student data
        student = get_object_or_404(Applicant_details, applicant_no=applicant_no)

        student.name = request.POST.get('applicant_name')
        student.application_no = request.POST.get('application_no')
        student.program = request.POST.get('programme')
        student.year_of_admission = request.POST.get('year_of_admission')
        student.roll_no = request.POST.get('roll_no')
        student.joining_date = request.POST.get('joining_date')
        student.leaving_date = request.POST.get('leaving_date')
        student.mobile_no = request.POST.get('mobile_no')
        student.email_id = request.POST.get('email')
        student.fathers_name = request.POST.get('father_name')
        student.mothers_name = request.POST.get('mother_name')
        student.phone_no_of_parents = request.POST.get('parent_phone_no')
        student.email_of_parents = request.POST.get('parent_email')
        student.address_of_parents = request.POST.get('address')
        student.local_guardian_name = request.POST.get('localguardian_name')
        student.local_guardian_mobile_no = request.POST.get('localguardian_mobile_no')
        student.deposit_amount = request.POST.get('deposit_amount')
        student.room_no = request.POST.get('room_number')
        student.bed_no = request.POST.get('bed_number')
        student.total_fees = request.POST.get('total_fees')
        student.fees_paid = request.POST.get('fees_paid')
        student.fees_remaining = request.POST.get('fees_remaining')

        # Save the updated data
        student.save()
        return redirect('hostel:students_details', user=user)
        return JsonResponse({'success': True, 'message': 'Student data updated successfully'})

def delete_user(request,user):
    if request.method == "POST":
        name = request.POST.get('namestd')
        applicant_no = request.POST.get('rollstd')

        userdetail = Applicant_details.objects.filter(Q(name=name) | Q(applicant_no=applicant_no)).first()
        userdetail.delete()
        return redirect('hostel:students_details', user=user)

    return redirect('hostel:dashboard', user=user)


def pay_fees(request,user):
    if request.method == 'POST':
        student_name = request.POST.get('std-name')
        include_mess = request.POST.get('includemess')
        fee_type = request.POST.get('feestype')
        total_amount = float(request.POST.get('totalamt', 0))
        transaction_type = request.POST.get('transactiontype')
        transaction_id = request.POST.get('tranID')
        if include_mess == "on":
            mess = True
        else:
            mess = False

        # Fetch the student's details from the database
        student = Applicant_details.objects.get(name=student_name)

        # Calculate remaining fees and update the database
        remaining_fees = float(student.fees_remaining) if student.fees_remaining else 0
        remaining_fees -= total_amount        

        # Save the payment transaction
        transaction = FeesTransaction.objects.create(
            applicant=student,
            name=student_name,
            # Admin_incharge = user,
            installment=fee_type,
            include_food=mess,
            final_amount=total_amount,
            transaction_method=transaction_type,
            transaction_id=transaction_id,
        )

        # Update the student's fees details
        student.fees_paid = float(student.fees_paid) + total_amount if student.fees_paid else total_amount
        student.fees_remaining = remaining_fees
        student.save()
        transaction.save()
        
        if total_amount == 4500:
            return redirect('https://rzp.io/l/ZfDdtO4IkF')  
        elif total_amount == 5000:
            return redirect('https://rzp.io/l/RlMXQjA ') 
        elif total_amount == 4000:
            return redirect('https://rzp.io/l/Ia9SgGN ') 
        elif total_amount == 3500:
            return redirect('https://rzp.io/l/YQDBEUuw71') 
        elif total_amount == 8500:
            return redirect('https://rzp.io/l/JSC0J1x9L7') 
        elif total_amount == 8000:
            return redirect('https://rzp.io/l/jguTricsXN ') 
        elif total_amount == 7500:
            return redirect('https://rzp.io/l/UHKfZvFh ') 
        elif total_amount == 7000:
            return redirect('https://rzp.io/l/o6bm4BL') 
        elif total_amount == 15000:
            return redirect('https://rzp.io/l/KG6iXXeIez') 
        elif total_amount == 13500:
            return redirect('https://rzp.io/l/x2JpOnTOJ') 
        elif total_amount == 12000:
            return redirect('https://rzp.io/l/EHaaL047w9') 
        elif total_amount == 10500:
            return redirect('https://rzp.io/l/2mWZtVTOcw') 
        elif total_amount == 25500:
            return redirect('https://rzp.io/l/edWcHUyoe') 
        elif total_amount == 24000:
            return redirect('https://rzp.io/l/9GRCDJIy') 
        elif total_amount == 22500:
            return redirect(' https://rzp.io/l/vpWWtdIbMU') 
        elif total_amount == 21000:
            return redirect('https://rzp.io/l/Km68OFk') 
        elif total_amount == 30000:
            return redirect('https://rzp.io/l/l7gEofF') 
        elif total_amount == 27000:
            return redirect('https://rzp.io/l/GFO84eaWkn') 
        elif total_amount == 24000:
            return redirect('https://rzp.io/l/LJAb1HTD') 
        elif total_amount == 21000:
            return redirect('https://rzp.io/l/X8VtALB') 
        elif total_amount == 51000:
            return redirect('https://rzp.io/l/FBoi7LO') 
        elif total_amount == 48000:
            return redirect('https://rzp.io/l/ODFBTskVAm') 
        elif total_amount == 45000:
            return redirect('https://rzp.io/l/atGlg2iipK') 
        elif total_amount == 42000:
            return redirect('https://rzp.io/l/4r2UVVdK') 
        elif total_amount == 60000 :
            return redirect('https://rzp.io/l/PQdayh9') 
        elif total_amount == 54000  :
            return redirect('https://rzp.io/l/kbREGtP0s') 
        elif total_amount == 48000 :
            return redirect('https://rzp.io/l/M69WMTy') 
        elif total_amount == 42000 :
            return redirect('https://rzp.io/l/t9LEbDG') 
        elif total_amount == 102000  :
            return redirect('https://rzp.io/l/OY0rOHgq7M') 
        elif total_amount == 96000 :
            return redirect('https://rzp.io/l/SDgExk3o') 
        elif total_amount == 90000  :
            return redirect('https://rzp.io/l/4csnNFJAD') 
        elif total_amount == 84000:
            return redirect('https://rzp.io/l/dfZcnM2XB')  
        
        context = {'user': user}
        return render(request, 'hostel/student_details.html', context )
        return JsonResponse({'success': True, 'message': 'Payment successful'})
    else:
        context = {'user': user}
        return render(request, 'hostel/student_details.html', context )
        return render(request, 'your_template.html')  # Replace 'your_template.html' with the actual template file


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
        # return JsonResponse({'message': 'task done'}, status=200)
        
    else:
        return redirect('/')       
    return redirect('hostel:dashboard', user=user)



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
    logged_in_user = user
    print(logged_in_user)
    hostel_details = Hostel_Details.objects.filter(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user)).first()
    if hostel_details:
        hostel_name = hostel_details.hostel_name
        room_numbers = HostelRoomDetails.objects.filter(hostel_name=hostel_name).values_list('room_no', flat=True)
        
    context = {'applicants': applicants , 'user': user , 'room_numbers': room_numbers}
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
        messages.success(request, 'Data saved successfully!')          
        context = {'hostel_name': hostel_name, 'user': user}
        return render(request, 'hostel/dashboard.html', context)
        # return JsonResponse({'status': 'success'})

    return redirect('hostel:dashboard', user=user)
def settings(request, user):
    logged_in_user = user
    hostel_details = Hostel_Details.objects.get(Q(hostel_warden_1=logged_in_user) | Q(hostel_warden_2=logged_in_user))
    print(hostel_details)
    hostel_id = hostel_details.Hostel_ID
    if request.method == 'POST':
        # hostel_name = request.POST.get('username')
        # hostel_address = request.POST.get('hosteladdress')
        hostel_capacity = request.POST.get('hostel_capacity')
        mess_vendor = request.POST.get('vendorname')
        mess_fees = request.POST.get('mess-fee')

        hostel_data = {
                # 'hostel_name': hostel_name if hostel_name  else None,
                # 'hostel_address': hostel_address if hostel_address  else None,
                'hostel_capacity': hostel_capacity if hostel_capacity  else None,
                'mess_vendor': mess_vendor if mess_fees else None,
                'mess_fees': mess_fees if mess_fees else None
            }

        if hostel_id:
            # If an ID is provided, update the existing record
            Hostel_Details.objects.filter(Hostel_ID=hostel_id).update(**hostel_data)
            messages.success(request, 'Data saved successfully!')  
            return render(request, 'hostel/dashboard.html', {'user': user})        
        
        else:
            # If no ID is provided, create a new record
            Hostel_Details.objects.create(**hostel_data)
    return render(request, 'hostel/settings.html', {'user': user, 'hostel_details':hostel_details})


    
def room_details(request, user):
    room_details = HostelRoomDetails.objects.all()
    return render(request, 'hostel/room_details.html', {'user': user, 'room_details': room_details})