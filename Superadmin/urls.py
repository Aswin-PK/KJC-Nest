from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),   
    path("adminsave/", views.adminsave, name="adminsave"),
    path('login', views.login_view, name='login'),
    # path('login/', views.login, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path("hostel_save/", views.hostel_save, name="hostel_save"),
    path("signup/", views.signup, name="signup"),
    path("sign/", views.signupuser, name="signupuser"),
    
]