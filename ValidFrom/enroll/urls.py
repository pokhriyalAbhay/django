from django.urls import path
from . import views

urlpatterns = [
    path('abhay/',views.show),
     path('sucess/',views.thankyou),
]
