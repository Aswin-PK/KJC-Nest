from django.urls import path
from . import views
from .views import adminsave

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.loginpage, name="login"),
    path("adminsave/", views.adminsave, name="adminsave"),
    path("hostel_save/", views.hostel_save, name="hostel_save"),
]