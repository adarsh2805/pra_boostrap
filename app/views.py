from django.http import request
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'home.html')

def pic(request):
    name="ARECANUT"
    return render(request,"second.html",{"name":name})
    
def details(request):
    return render(request,'details.html') 