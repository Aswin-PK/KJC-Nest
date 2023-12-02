from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser,AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, usertype='User', status='Active'):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, usertype=usertype, status=status)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password=password, usertype='Super_admin')
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128) 
    mobile = models.CharField(max_length= 50 , null=True)
    USERTYPE_CHOICES = [
        ('Super_admin', 'Super_admin'),
        ('Hostel_admin', 'Hostel_admin'),
        ('Guest_admin', 'Guest_admin'),
        ('User', 'User'),
    ]
    usertype = models.CharField(max_length=20, choices=USERTYPE_CHOICES, default='User', null=False)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Assigned', 'Assigned'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active', null=False)

    # Additional fields for managing user permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',  # Add a related_name to avoid clash
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',  # Add a related_name to avoid clash
        related_query_name='user'
    )

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email
    
# Applicant details loaded from excel
class Hostel_Details(models.Model):
    Hostel_ID = models.AutoField(
        
        primary_key=True,
        null= False
    )
    hostel_name = models.CharField(
        max_length=255,
        null= False
    )      
    hostel_capacity = models.CharField(
        max_length=100, null= False,
        default="Not Defined"
    )
    hostel_warden_1 = models.CharField(
        max_length=100,
        null= False
    )
    hostel_warden_2 = models.CharField(
        max_length=100,
        null= True
    )
    hostel_address = models.TextField(
        null= False
    )
    mess_vendor = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    mess_fees = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    hostel_image = models.ImageField(
        null=True,
        default="image not available"
    )

    def __str__(self):
        return self.hostel_name
    


class HostelRoomDetails(models.Model):
    BED_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    ]

    hostel_name = models.CharField(
        max_length=255,
        null=False
    )
    room_no = models.CharField(max_length=20, unique=True)
    no_of_beds = models.CharField(choices=BED_CHOICES , max_length=255)
    bed_no1_id = models.CharField(max_length=10)
    bed_no1_price = models.CharField(max_length=255, null=False,default="5000")
    bed_no2_id = models.CharField(max_length=10, blank=True, null=True)
    bed_no2_price = models.CharField(max_length=255,blank=True, null=True)
    bed_no3_id = models.CharField(max_length=10, blank=True, null=True)
    bed_no3_price = models.CharField(max_length=255,blank=True, null=True)
    bed_no4_id = models.CharField(max_length=10, blank=True, null=True)
    bed_no4_price = models.CharField(max_length=255,blank=True, null=True)
    bathroom_attached = models.BooleanField()

    def __str__(self):
        return f"{self.hostel_name} - Room {self.room_no}"

class Applicant_details(models.Model):
    # Personal Information
    name = models.CharField(max_length=255)
    applicant_no = models.CharField(max_length=10, unique=True)
    program_choices = [
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate'),
    ]
    program = models.CharField(max_length=20, choices=program_choices)
    year_of_admission = models.IntegerField(choices=[(year, year) for year in range(2000, 2050)])
    roll_no = models.CharField(max_length=20, blank=True, null=True)

    # Hostel Stay Information
    joining_date = models.DateField()
    leaving_date = models.DateField(null=True, blank=True)
    mobile_no = models.CharField(max_length=15)
    email_id = models.EmailField()

    # Parent/Guardian Information
    fathers_name = models.CharField(max_length=255)
    mothers_name = models.CharField(max_length=255)
    phone_no_of_parents = models.CharField(max_length=15)
    email_of_parents = models.EmailField()
    address_of_parents = models.TextField()

    # Local Guardian Information
    local_guardian_name = models.CharField(max_length=255)
    local_guardian_mobile_no = models.CharField(max_length=15)

    # Financial Information
    deposit_amount = models.CharField(max_length=255,blank=True, default="Null" )
    hostel_name = models.CharField(max_length=255, default="Null" , null= False)
    user_registered = models.CharField(max_length=255, default="Null" , null= False)
    room_no = models.CharField(max_length=10, null=True, blank=True)
    bed_no = models.CharField(max_length=5, null=True, blank=True)
    total_fees = models.CharField(null=True, max_length=255,blank=True, default="Null" )
    fees_paid = models.CharField(null=True,max_length=255,blank=True, default="Null")
    fees_remaining = models.CharField(null=True,max_length=255,blank=True, default="Null")

    def __str__(self):
        return f"{self.applicant_no} - {self.name}"


class FeesTransaction(models.Model):
    # ForeignKey to Applicant_Details
    applicant = models.ForeignKey(Applicant_details, on_delete=models.CASCADE)

    # Transaction Details
    name = models.CharField(max_length=255 )
    Admin_incharge = models.CharField(max_length=50,null=False,default="Admin")
    # total_fees = models.CharField(max_length=255,blank=True, default="Null")
    installment_choices = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half Yearly', 'Half Yearly'),
        ('Yearly', 'Yearly'),
    ]
    installment = models.CharField(max_length=50, choices=installment_choices)
    include_food = models.BooleanField()
    final_amount = models.CharField(max_length=255,blank=True, default="Null")

    # Transaction Method
    TRANSACTION_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('NetBanking', 'NetBanking'),
        ('Debit_Card', 'Debit_Card'),
        ('Credit_Card', 'Credit_Card'),
        ('Paytm', 'Paytm'),
        ('PhonePay', 'PhonePay'),
        ('GooglePay', 'GooglePay'),
    ]
    transaction_method = models.CharField(max_length=20, choices=TRANSACTION_METHOD_CHOICES)

    # Transaction ID (Applicable for Digital Payment Methods)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.applicant_no} - {self.name}"
    
# Applicant details loaded from excel
class Guestroom_Details(models.Model):
    Guestroom_ID = models.AutoField(
        
        primary_key=True,
        null= False
    )
    Guestroom_name = models.CharField(
        max_length=255,
        null= False
    )      
    Guestroom_capacity = models.CharField(
        max_length=100, null= False,
        default="Not Defined"
    )
    Guestroom_admin_1 = models.CharField(
        max_length=100,
        null= False
    )
    Guestroom_admin_2 = models.CharField(
        max_length=100,
        null= True
    )
    Guestroom_address = models.TextField(
        null= False
    )  


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    
    ext = os.path.splitext(value.name)[1]
    validex = ['.png' , '.jpg' , '.jpeg' , '.pdf']
    if not ext.lower() in validex:
        raise ValidationError("Unsupported File Extension. please upload '.png' , '.jpg' , '.jpeg' , '.pdf'")

class Guestroomuserdetails(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Request', 'Request'),
        ('Awaiting', 'Awaiting'),
        ('Confirm', 'Confirm'),
    ]
    NOTIFICATION_CHOICES = [
        ('Accept', 'Accept'),
        ('Reject', 'Reject'),
    ]
    name = models.CharField(max_length=255)
    email_1 = models.EmailField()
    email_2 = models.EmailField(blank=True, null=True)
    mobile_no = models.CharField(max_length=15)
    address_proof = models.FileField(upload_to='proofimage/', validators=[validate_file_extension], blank=True)
    reason_of_visiting = models.CharField(max_length=20, null=False , default='Other')
    date_of_birth = models.DateField(null=True, default=None)
    date_of_checkin = models.DateField(null=False)
    date_of_checkout = models.DateField(null=False)
    room_type = models.CharField(max_length=50)
    final_amount = models.CharField(max_length=10)
    discount = models.CharField(max_length=5, default=0)
    paid_amount = models.CharField(max_length=10, default=0)
    room_number = models.CharField(max_length=10)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='Request')
    notification = models.CharField(max_length=10, choices=NOTIFICATION_CHOICES, default='Accept')    
    
    
    
class GuestRoomcreation(models.Model):
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Dormetry', 'Dormetry'),
        ('AC_Single', 'AC_Single'),
        ('AC_Double', 'AC_Double'),
    ]
    BED_CHOICES = [
        (1, '1'),
        (2, '2'),
    ]
    ROOM_STATUS_CHOICES = [
        (True, 'Booked'),
        (False, 'Vacant'),
    ]
    Guestroom_name = models.CharField(
        max_length=255,
        null= False,
        default='null'
    ) 
    Guestroom_bed_count = models.IntegerField(choices=BED_CHOICES)
    Guestroom_room_number = models.CharField(max_length=10, unique=True)
    Guestroom_room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='single')
    Guestroom_with_AC = models.BooleanField(default=False)
    Guestroom_price = models.DecimalField(max_digits=10, decimal_places=2)
    Guestroom_is_booked = models.BooleanField(choices=ROOM_STATUS_CHOICES, default=False)
    
    
class Notification(models.Model):
    user = models.CharField(max_length=20,null=False,default="User")
    reason_of_visiting = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at =  models.BooleanField(default=True)