from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),  
    # path("login/",views.loginpage,name='loginpage'),  
    path("adminsave/", views.adminsave, name="adminsave"),
<<<<<<< HEAD
    path('login', views.login_view, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('/', views.hostelcreation, name='hostelcreation'),
=======
    path('/', views.login_view, name='login'),    
>>>>>>> 97ab1d53820533f4694bcb26960e8d7d8aa02c6a
    path("hostel_save/", views.hostel_save, name="hostel_save"),
    
]