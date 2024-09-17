from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def show(request):
    fm = StudentRegistration()
    fm.order_fields(field_order=['first_name','email','name'])
    return render(request,'enroll/user.html',{'form':fm})
