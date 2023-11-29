from django.urls import path
from . import views

app_name = 'hostel'
urlpatterns = [
    path("<str:user>", views.dashboard, name="dashboard"),
    path("<str:user>/students_details/", views.students_details, name="students_details"),
    path('<str:user>/transactions/', views.transactions, name="transactions"),
    path('<str:user>/fee_payment/', views.fee_payment, name="fee_payment"),
    path("<str:user>/hroomsave/", views.hroomsave, name="hroomsave"),
    path("<str:user>/settings/", views.settings, name="settings"),
]