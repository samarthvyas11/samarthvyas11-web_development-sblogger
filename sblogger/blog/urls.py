from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path("postComment",views.postComment, name = "postComment"),
    path("uploadblog",views.uploadblog,name = "uploadblog"),
    path('<str:slug>/',views.blogpost, name = "blogpost"),
]