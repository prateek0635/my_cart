from django.contrib import admin
from django.urls import path
from MyApp import views


urlpatterns = [
    path('', views.index ,name='Index'),
    path('login', views.loginuser ,name='Login'),
    path('createuser', views.createuser ,name='SignUp'),
    path('logout', views.logoutuser ,name='Logout'),
    path('shopview/<int:shopid>', views.Myshop ,name='Myshop'),
    path('shopview/addprod/<int:shopid>', views.add_prod ,name='Add'),
    path('productupdate/<int:shopid>', views.product_update ,name='Update'),
    path('productupdate/deleteProd/<int:prodid>', views.delete_prod ,name='delete'),
    path('updateprice/<int:prodid>', views.update_price ,name='Update_price'),
    path('addtocart/<int:prodid>/<str:cmd>/', views.add_to_cart ,name='Add_To_Cart'),
    path('order/<int:shopid>', views.order_cart ,name='Order'),
    path('ordertracker', views.order_tracker ,name='Order_Tracker'),
    path('orders/<int:shopid>', views.orders_for_shop ,name='orders_for_shop'),
]