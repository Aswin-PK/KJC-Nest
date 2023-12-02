from django.urls import path
from . import views


app_name = 'guesthouse'
urlpatterns = [
    path("<str:user>", views.dashboard, name="dashboard"),
    path("<str:user>/groomsave/", views.groomsave, name="groomsave"),
    path("<str:user>/my_bookings/", views.my_bookings, name="my_bookings"),
    path("<str:user>/", views.user_dashboard, name="user_dashboard"),
    path("<str:user>/userrequest/", views.userrequest, name="userrequest"),
    path('logout', views.logoutUser, name='logout'),
    path("<str:user>/my_accounts/", views.my_accounts, name="my_accounts"),
]