from django.contrib import admin
from .models import Notification,Guestroom_Details,Guestroomuserdetails,GuestRoomcreation,Hostel_Details,FeesTransaction, HostelRoomDetails,Applicant_details,CustomUser

# Register your models here.
admin.site.register(Hostel_Details)
admin.site.register(HostelRoomDetails)
admin.site.register(Applicant_details)
admin.site.register(FeesTransaction)
admin.site.register(CustomUser)
admin.site.register(GuestRoomcreation)
admin.site.register(Guestroomuserdetails)
admin.site.register(Guestroom_Details)



class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reason_of_visiting', 'is_read', 'created_at')
    list_filter = ('is_read',)

admin.site.register(Notification, NotificationAdmin)