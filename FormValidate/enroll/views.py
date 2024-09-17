from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def show(request):
    if request.method == 'POST' :
        fm = StudentRegistration(request.POST)
        #print("post se aay hain ")
        #print(fm)
        if fm.is_valid():
         print("form validate")
         print('name:',fm.cleaned_data['name'])
         print('email:',fm.cleaned_data['email'])


    else:
        fm = StudentRegistration()
        print("yeh get se aaya hain")
    
    fm = StudentRegistration()
   # fm.order_fields(field_order=['first_name','email','name'])
    return render(request,'enroll/user.html',{'form':fm})
