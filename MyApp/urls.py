from django.contrib import admin
from django.urls import path
from MyApp import views


urlpatterns = [
    path('', views.index ,name='Index'),
    path('login', views.loginuser ,name='Login'),
    path('createuser', views.createuser ,name='SignUp'),
    path('logout', views.logoutuser ,name='Logout'),
    path('shopview/<int:shopid>', views.Myshop ,name='Myshop'),
    path('shopview/addprod/<int:shopid>', views.add_prod ,name='Add')    
]