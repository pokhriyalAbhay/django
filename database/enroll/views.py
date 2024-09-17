from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
def show(request):
    if request.method == 'POST' :
        fm = StudentRegistration(request.POST)
        #print("post se aay hain ")
        #print(fm)
        if fm.is_valid():
          nm =  fm.cleaned_data['name']
          em =  fm.cleaned_data['email']
          reg = User(name = nm,email = em)
          reg.save()


    else:
        fm = StudentRegistration()
        print("yeh get se aaya hain")
    
    fm = StudentRegistration()
   # fm.order_fields(field_order=['first_name','email','name'])
    return render(request,'enroll/user.html',{'form':fm})
