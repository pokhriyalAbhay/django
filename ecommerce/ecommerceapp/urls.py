from django.urls import path
from django.views import View
from ecommerceapp import views
urlpatterns = [
    path('',views.index,name="index"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
]
