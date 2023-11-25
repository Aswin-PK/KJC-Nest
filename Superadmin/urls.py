from django.urls import path
from . import views
from .views import adminsave

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.loginpage, name="login"),
    path("adminsave/", views.adminsave, name="adminsave"),
    path('/', views.login_view, name='login'),
]