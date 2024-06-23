from django.shortcuts import render
from django.shortcuts import HttpResponse
def userdetails(request):
    return render(request,"home.html")
def login_page(request):
    return render(request,"login.html")


