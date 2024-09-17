from . import views
from django.urls import path

urlpatterns = [
    path('fees/', views.fees_django),
]
