from django.contrib import admin
from django.urls import path
from MyApp import views


urlpatterns = [
    path('', views.index ,name='Index'),
    path('shops', views.index_shop ,name='IndexShop'),
    path('login', views.loginuser ,name='Login'),
    path('createuser', views.createuser ,name='SignUp'),
    path('logout', views.logoutuser ,name='Logout'),
    path('shops/<str:shop_id>', views.Myshop ,name='Myshop'),
    path('shops/addprod/<int:shopid>', views.add_prod ,name='Add'),
    path('productupdate/<int:shopid>', views.product_update ,name='Update'),
    path('productupdate/deleteProd/<int:prodid>', views.delete_prod ,name='delete'),
    path('updateprice/<int:prodid>', views.update_price ,name='Update_price'),
    path('addtocart/<int:prodid>/<str:cmd>/', views.add_to_cart ,name='Add_To_Cart'),
    path('order/<int:shopid>', views.order_cart ,name='Order'),
    path('ordertracker', views.order_tracker ,name='Order_Tracker'),
    path('orders/<int:shopid>', views.orders_for_shop ,name='orders_for_shop'),
    path('orders_update/<int:orderid>', views.order_update ,name='order_update'),
    path('search/', views.search ,name='search'),
    path('contact/', views.contact_us ,name='contact'),
    path('blog/', views.blog_home ,name='blog_home'),
    path('blog/<slug:slug>', views.blog_full ,name='blog_full'),
    path('rate/<int:id>', views.rate ,name='rate'),
    path('rateprod/<int:id>', views.rateprod1 ,name='rateprod'),
    path('reviews/<int:id>', views.all_review ,name='reviews'),
    path('productreview/<slug:slug>', views.all_prod_rev ,name='all_prod_rev'),
    path('full/<slug:slug>', views.fullprod ,name='fullprod'),
    path('addcategory/<str:com>', views.addcategory ,name='addcategory'),
    # path('readblog/<int:id>', views.blog_home ,name='readBlog'),
    
]