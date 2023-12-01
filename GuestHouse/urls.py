from django.urls import path
from . import views


app_name = 'guesthouse'
urlpatterns = [
    path("<str:user>", views.dashboard, name="dashboard"),
    path("<str:user>/groomsave/", views.groomsave, name="groomsave"),
]