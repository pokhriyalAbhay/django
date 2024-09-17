from django.shortcuts import render

# Create your views here.
#def show_detail(request,my_id):
    #print(my_id)
   # return render(request,'enroll/index.html',{'id':my_id})
def show_detail(request,my_id):
    #print(my_id)
   if(my_id==1):
       student = {"id":my_id,"name":"rohan"}
   if(my_id==3):
       student = {"id":my_id,"name":"abhay"}
   if(my_id==2):
     student = {"id":my_id,"name":"abhi"}
       
   return render(request,'enroll/index.html',student)
def base(request):
    return render(request,'enroll/home.html')