from . import views
from django.urls import path

urlpatterns = [
    path('learn/', views.django),
]
