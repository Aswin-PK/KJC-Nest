from django.db import models

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

    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    visiting_reason = models.CharField(max_length=20, choices=VISITING_REASON_CHOICES)
    id_proof = models.CharField(max_length=20, choices=ID_PROOF_CHOICES)
    id_proof_uploaded = models.FileField(upload_to='id_proofs/')
    room_type = models.CharField(max_length=50)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notification = models.CharField(max_length=10, choices=NOTIFICATION_CHOICES)
    room_no = models.CharField(max_length=10)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES)

    def __str__(self):
        return self.name
