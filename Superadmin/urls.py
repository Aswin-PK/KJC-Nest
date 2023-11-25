from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.loginpage, name="login"),
    path("adminsave/", views.adminsave, name="adminsave"),
    path('/', views.login_view, name='login'),
    path('/', views.hostelcreation, name='hostelcreation'),
    
]