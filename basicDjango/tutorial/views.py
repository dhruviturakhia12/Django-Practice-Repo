from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello! You're at the home finally.")
    return render(request,'home.html',{'name':'Dhruvi'})
def about(request):
    return render(request,'home.html',{'name':'Misha'})
    # return render(request,'home.html')
def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1 + val2
    return render(request,'result.html',{'result':res})
    # return render(request,'home.html')
def sub(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1 - val2
    return render(request,'result.html',{'result':res})

def contact(request):
    return HttpResponse("Hello from contact!")
    # return render(request,'home.html')
def blog(request):
    return HttpResponse("Hello from blog!")
    # return render(request,'home.html')
