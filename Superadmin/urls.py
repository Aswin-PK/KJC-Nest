from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),  
    # path("login/",views.loginpage,name='loginpage'),  
    path("adminsave/", views.adminsave, name="adminsave"),
    path('login', views.login_view, name='login'),
    path('logout', views.logoutUser, name='logout'),
    # path('/', views.hostelcreation, name='hostelcreation'),
    path("hostel_save/", views.hostel_save, name="hostel_save"),
    
]