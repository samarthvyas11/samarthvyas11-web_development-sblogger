from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('', views.home, name='home'),
    path("search",views.search,name="search"),
    path("signup",views.handlesignup,name="handlesignup"),
    path("login",views.handlelogin,name="handlelogin") ,
    path("logout",views.handlelogout,name="handlelogout"),
    path("createblog",views.createblog,name="createblog"),
 
]
