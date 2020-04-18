from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import myclass,shop,products
# from .forms import *

# Create your views here.
def index(request):
    data=shop.objects.all()
    print(data)
    try:
        prams={'name':request.user.first_name,'data':data,'range':3}
    except:
        prams={'data':data,'range':range(1,3)}
    
    return render(request,'index.html',prams)

def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        passw=request.POST['password']
        user=authenticate(username=username, password=passw)
        # print(username,passw)
        if user is not None:
            login(request,user)
            return redirect('/')
    # A backend authenticated the credentials
        else:
            messages.error(request, 'Wrong Password or Email Try again')
            return redirect('/login')


    # No backend authenticated the credentials
    return render(request,'login.html')

def createuser(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        pass1=request.POST['pass']
        pass2=request.POST['passw']

        # print(first_name,last_name,email,pass1,pass2)
        if pass1!=pass2:
            # print("Nope")
            messages.error(request, 'Password Mismatch')
            return redirect('/createuser')
        else:
            try:
                user = User.objects.create_user(username=email,email=email,password=pass1,first_name=first_name,last_name=last_name)
                user.save()
                login(request,user)
                return redirect('/')
            except:
                messages.error(request, 'User Already Exists Try with a diffrent Email ID')
                return redirect('/createuser')
            
            
    return render(request,'signup.html')

def logoutuser(request):
    logout(request)
    messages.error(request, 'LoggedOut')
    return redirect('/login')
#This fucnction shows the products
def Myshop(request,shopid):
    prod=products.objects.filter(shop=shopid)
    shopn=shop.objects.filter(id=shopid)[0]

    param={'prod':prod,'shop':shopn}
    if request.user==shopn.shop_user:
        param['owner']=True
        print(param)
    return render(request,'shop.html',param)


#function the adding the product by the 

def add_prod(request,shopid):
    shopn=shop.objects.filter(id=shopid)[0]
    print(request.user,shopn)
    if request.user==shopn.shop_user:
        if request.method=='POST':
            prod_name=request.POST['Product_name']
            prod_disc=request.POST['prod_disc']
            prod_price=request.POST['prod_price']
            Img=request.FILES
            prod_img=Img.get("prod_img")
            print(prod_img)
            print(prod_name,prod_disc,prod_price,prod_disc,prod_img)
            add=products.objects.create(shop=shopn,prod_name=prod_name,prod_disc=prod_disc,
                prod_price=prod_price,prod_img=prod_img)
            add.save()
            messages.success(request, 'Updated')
            return redirect(f'/shopview/{shopn.id}')
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')
    

    param={'shop':shopn}
    return render(request,'add_prod.html',param)