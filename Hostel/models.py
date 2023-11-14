from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Login details
class User(models.Model):
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