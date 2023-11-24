from django.contrib import admin
from .models import Hostel_Details,FeesTransaction, HostelRoomDetails,Applicant_details,CustomUser

# Register your models here.
admin.site.register(Hostel_Details)
admin.site.register(HostelRoomDetails)
admin.site.register(Applicant_details)
admin.site.register(FeesTransaction)
admin.site.register(CustomUser)