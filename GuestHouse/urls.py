from django.urls import path
from . import views


app_name = 'guesthouse'
urlpatterns = [
    path("<str:user>", views.dashboard, name="dashboard"),
    path("<str:user>/groomsave/", views.groomsave, name="groomsave"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("my_accounts/", views.my_accounts, name="my_accounts"),
]