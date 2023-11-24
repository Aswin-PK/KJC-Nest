from django.urls import path
from . import views
from .views import adminsave

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.loginpage, name="login"),
    path("update_hostel/<int:Hostel_ID>/", views.update_hostel, name="update_hostel"),
    path("adminsave/", views.adminsave, name="adminsave"),
]