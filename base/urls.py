from django.contrib import admin
from django.urls import path 
from .views import userdetails,login_page,trys,api_for_all_custmor

urlpatterns = [

    path("",userdetails,name="home_page"),
    path("login_page",login_page,name="login_page"),
    path("try",trys,name="trys"),
    path("api",api_for_all_custmor,name="api")
    
]