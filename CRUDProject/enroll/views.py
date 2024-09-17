from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from .models import User
# this function will Add new item and show all the items
def add_show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            fm.save()
            fm = Student()
    else:
         fm = Student()
    stud = User.objects.all()
    return render(request,'enroll/index.html',{'form': fm,'stu':stud})
#this function will delete the data 
def delete_data(request,id):
    if request.method  == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
#this function will update and edit the item 
def update_data(request,id):
    return render(request,'enroll/updatefile.html')