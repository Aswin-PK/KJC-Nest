from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
]