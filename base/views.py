from django.shortcuts import render
from django.shortcuts import HttpResponse
from .import utils
from django.contrib.auth.hashers import make_password,check_password
from .import models
def userdetails(request):
    return render(request,"home.html")
def login_page(request):
    return render(request,"login.html")
def trys(request):
    data=request.POST.dict()
    password=make_password(data["password"])
    update_data={}
    for key,values in data.items():
        if key=="confirm_password" or key=="csrfmiddlewaretoken":
            continue
        update_data[key]=values
    update_data["password"]=password
    custmor=models.Customer(**update_data)
    custmor.save()
    data={"sub":data["first_name"]}
    jwt_token=utils.create_acess_token(data)
    return HttpResponse(jwt_token)
    

def api_for_all_custmor(request):
    x=models.Customer.objects.all()
    x=[[x.password,x.last_name] for x in x]
    return HttpResponse(x)






# Create your views here.
