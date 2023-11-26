from django.urls import path
from . import views

urlpatterns = [
    path("<str:user>/", views.dashboard, name="dashboard"),
    path('transactions/', views.transactions, name="transactions"),
    path('fee_payment/', views.fee_payment, name="fee_payment"),
    path("<str:user>/hroomsave/", views.hroomsave, name="hroomsave"),
] 