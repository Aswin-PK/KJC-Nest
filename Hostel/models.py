from django.db import models
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
        ('Super_admin', 'Super Admin'),
        ('Hostel_Admin', 'Hostel Admin'),
        ('Guest_Admin', 'Guest Admin'),
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
    
# class CustomUser(models.Model):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=128) 
#     mobile = models.CharField(max_length= 50 , null=True)

#     usertype = models.CharField(max_length=20, default='User', null=False)
#     STATUS_CHOICES = [
#         ('Active', 'Active'),
#         ('Inactive', 'Inactive'),
#         ('Assigned', 'Assigned'),
#     ]
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active', null=False)
#     # date_joined = models.DateTimeField(auto_now_add=True)
#     # Additional fields for managing user permissions
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    

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
    mess_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True, null=True
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
    no_of_beds = models.IntegerField(choices=BED_CHOICES)
    bed_no1_id = models.CharField(max_length=10)
    bed_no1_price = models.DecimalField(max_digits=10, decimal_places=2)
    bed_no2_id = models.CharField(max_length=10, blank=True, null=True)
    bed_no2_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bed_no3_id = models.CharField(max_length=10, blank=True, null=True)
    bed_no3_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bed_no4_id = models.CharField(max_length=10, blank=True, null=True)
    bed_no4_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bathroom_attached = models.BooleanField()

    def __str__(self):
        return f"{self.hostel_name} - Room {self.room_no}"

class Applicant_details(models.Model):
    # Personal Information
    name = models.CharField(max_length=255)
    applicant_no = models.CharField(max_length=10, unique=True)
    program_choices = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]
    program = models.CharField(max_length=2, choices=program_choices)
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
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    hostel_name = models.CharField(max_length=255, default="Null")
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=5)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fees_remaining = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.applicant_no} - {self.name}"


class FeesTransaction(models.Model):
    # ForeignKey to Applicant_Details
    applicant = models.ForeignKey(Applicant_details, on_delete=models.CASCADE)

    # Transaction Details
    name = models.CharField(max_length=255)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    installment_choices = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half Yearly', 'Half Yearly'),
        ('Yearly', 'Yearly'),
    ]
    installment = models.CharField(max_length=50, choices=installment_choices)
    include_food = models.BooleanField()
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Transaction Method
    TRANSACTION_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('NetBanking', 'NetBanking'),
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Paytm', 'Paytm'),
        ('PhonePay', 'PhonePay'),
        ('GooglePay', 'GooglePay'),
    ]
    transaction_method = models.CharField(max_length=20, choices=TRANSACTION_METHOD_CHOICES)

    # Transaction ID (Applicable for Digital Payment Methods)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.applicant_no} - {self.name}"
