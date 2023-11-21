from django.db import models
from django.utils import timezone

# Create your models here.
class RoomDetail(models.Model):
    ROOM_TYPE_CHOICES = [
        ('dormitory', 'Dormitory'),
        # Add more choices if needed
    ]

    room_no = models.CharField(max_length=10, unique=True)
    no_of_bed = models.IntegerField(choices=[(1, '1'), (2, '2')])
    ac_non = models.BooleanField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES, default='dormitory')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_no} - {self.room_type}"


class UserDetail(models.Model):
    VISITING_REASON_CHOICES = [
        ('Business', 'Business'),
        ('Leisure', 'Leisure'),
        ('Other', 'Other'),
    ]

    ID_PROOF_CHOICES = [
        ('Aadhar', 'Aadhar Card'),
        ('Passport', 'Passport'),
        ('DriverLicense', 'Drivers License'),
        ('Other', 'Other'),
    ]

    NOTIFICATION_CHOICES = [
        ('Accept', 'Accept'),
        ('Reject', 'Reject'),
    ]

    BOOKING_STATUS_CHOICES = [
        ('Request', 'Request'),
        ('Awaiting', 'Awaiting'),
        ('Confirm', 'Confirm'),
    ]

    name = models.CharField(max_length=255, default='')
    email = models.EmailField(default='')
    mobile_no = models.CharField(max_length=15, default='')
    visiting_reason = models.CharField(max_length=20, choices=VISITING_REASON_CHOICES, default='Other')
    id_proof = models.CharField(max_length=20, choices=ID_PROOF_CHOICES, default='Other')
    id_proof_uploaded = models.FileField()
    room_type = models.CharField(max_length=50, default='')
    room_no = models.CharField(max_length=10, default='')
    checkin_date = models.DateField(default=timezone.now)
    checkout_date = models.DateField(default=timezone.now)
    original_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    notification = models.CharField(max_length=10, choices=NOTIFICATION_CHOICES, default='Accept')
    
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='Request')

    def save(self, *args, **kwargs):
        # Ensure checkin_date is at least 3 days from today
        if self.checkin_date and (self.checkin_date - timezone.now().date()).days < 3:
            raise ValueError("Checkin date must be at least 3 days from today.")
        
        # If checkout_date is not provided, set it as 1 day after checkin_date
        if self.checkin_date and not self.checkout_date:
            self.checkout_date = self.checkin_date + timezone.timedelta(days=1)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
