from django.shortcuts import render
# Create your views here.
def fees_django(request):
    return render(request,'fees/fees1.html',{'fee':'150 ruprees and extra charge '})
