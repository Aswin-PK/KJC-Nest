from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('transactions/', views.transactions, name="transactions"),
    path('fee_payment/', views.fee_payment, name="fee_payment"),
]