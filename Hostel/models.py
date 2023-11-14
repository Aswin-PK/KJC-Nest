from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Login details
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        primary_key=True
    )
    username = models.CharField(
        max_length= 100,
        null = False
    )
    password = models.CharField(
        max_length= 50,
        null = False
    )
    user_type = models.CharField(
        max_length=100,
        null=False
    )

    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
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
    hostel_warden = models.CharField(
        max_length=100,
        null= False
    )
    hostel_address = models.TextField(
        null= False
    )
    mess_vendor = models.CharField(
        max_length=255,
        null= False
    )
    mess_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null= False
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

class Applicant_Details(models.Model):
    # Personal Information
    name = models.CharField(max_length=255)
    applicant_no = models.CharField(max_length=10, unique=True)
    program_choices = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]
    program = models.CharField(max_length=2, choices=program_choices)
    year_of_admission = models.IntegerField(choices=[(year, year) for year in range(2000, 2030)])
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
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=5)
    total_fees = models.DecimalField(max_digits=10, decimal_places=2)
    fees_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fees_remaining = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.applicant_no} - {self.name}"
