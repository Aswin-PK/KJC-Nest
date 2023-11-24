from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.loginpage, name="login"),
    path("update_hostel/<int:Hostel_ID>/", views.update_hostel, name="update_hostel"),
]