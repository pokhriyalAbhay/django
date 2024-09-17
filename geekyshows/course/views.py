from django.shortcuts import render

def django(request):
    return render(request,'course/course1.html',{'nm':'django-course'})
