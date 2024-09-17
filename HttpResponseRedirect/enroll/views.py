from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.
def thankyou(request):
   return render(request,'enroll/sucess.html')
def show(request):
    if request.method == 'POST' :
        fm = StudentRegistration(request.POST)
        #print("post se aay hain ")
        #print(fm)
        if fm.is_valid():
         name = fm.cleaned_data['name']
         email = fm.cleaned_data['email']
         print("form validate")
         print('name:',name)
         print('email:',email)
         return HttpResponseRedirect('/regi/sucess/')


    else:
        fm = StudentRegistration()
        print("yeh get se aaya hain")
    
    fm = StudentRegistration()
   # fm.order_fields(field_order=['first_name','email','name'])
    return render(request,'enroll/user.html',{'form':fm})
