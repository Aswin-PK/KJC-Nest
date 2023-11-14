from django.contrib import admin
from .models import Hostel_Details, HostelRoomDetails, User

# Register your models here.
admin.site.register(Hostel_Details)
admin.site.register(HostelRoomDetails)
admin.site.register(User)