from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import shop,products,cart,order,contact,myblog,rateing,category_prod,rateprod
from django.contrib.auth.decorators import login_required
from django.db.models import Avg,Count
from django.utils.text import slugify
import string , random
from MyApp.forms import prodabout
# from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def index_shop(request):
    data=shop.objects.all()   
    try:
        prams={'name':request.user.first_name,'data':data,'range':3}
    except:
        prams={'data':data,'range':range(1,3)}
    return render(request,'shop_home.html',prams)

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
def Myshop(request,shop_id):
    shop1=shop.objects.filter(shop_id=shop_id)[0]
    shopid=shop1.id
    prod=products.objects.filter(shop=shopid)
    shopn=shop.objects.filter(id=shopid)[0]
    rate=rateing.objects.filter(shop=shopid)
    avg=rateing.objects.filter(shop=shopid).aggregate(Avg('rate'))
    shopn.clicks=shopn.clicks+1
    shopn.save()
    category=category_prod.objects.filter(shop=shopn)
    con=0
    param={'prod':prod,'shop':shopn,'rate':rate,"category":category}
    if avg['rate__avg'] is None:
        avg['rate__avg']=5
    shopn.rating=round(avg['rate__avg'],1)
    shopn.save()
    param['rate__avg']=round(avg['rate__avg'],1)
    if param['rate__avg']>=3.5:
        param['rate_col']='success'
    elif  param['rate__avg']>=2.5:
        param['rate_col']='warning'
    else:
        param['rate_col']='danger'
    if not request.user.is_anonymous:
        a=cart.objects.filter(user=request.user,shop=shopn)
        param['cart']=a
        for i in a:
            con+=1
        
        param['count']=con
    if request.user==shopn.shop_user:
        param['owner']=True
    return render(request,'shop.html',param)


#function the adding the product by the 

def add_prod(request,shopid):
    shopn=shop.objects.filter(id=shopid)[0]
    # print(request.user,shopn)
    if request.user==shopn.shop_user:
        if request.method=='POST':
            prod_name=request.POST['Product_name']
            prod_disc=request.POST['prod_disc']
            cate1=request.POST['cate']
            category=category_prod.objects.filter(id=cate1)[0]
            prod_price=request.POST['prod_price']
            MRP=request.POST['mrp']
            Img=request.FILES
            prod_img=Img.get("prod_img")
            slug=slugify(prod_name)
            discount=((int(MRP)-int(prod_price))/int(MRP))*100
            ex=products.objects.filter(slug=slug)
            if ex.exists():
                rand=''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
                slug=slug + '-' + str(rand)
            
            add=products.objects.create(shop=shopn,prod_name=prod_name,prod_disc=prod_disc,
                prod_price=prod_price,MRP=MRP,slug=slug,category_n=category,prod_img=prod_img,discount=discount)
            add.save()
            form=prodabout(request.POST,instance=add)
            if form.is_valid():
                post_item=form.save(commit=False)
                post_item.save()
            
            messages.success(request, 'Updated')
            return redirect(f'/shops/{shopn.shop_id}')
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')
    
    category=category_prod.objects.filter(shop=shopn)
    form=prodabout()
    param={'shop':shopn,"category":category,'form':form}
    return render(request,'add_prod.html',param)



def product_update(request,shopid):
    shopn=shop.objects.filter(id=shopid)[0]
    prod=products.objects.filter(shop=shopid)
    category=category_prod.objects.filter(shop=shopn)
    if request.user==shopn.shop_user:
        param={'prod':prod,'shop':shopn,"category":category}
        return render(request,'product_update.html',param)
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')
    
def update_price(request,prodid):
    a=products.objects.filter(id=prodid)[0]
    shop=a.shop
    print(shop)
    if request.user==a.shop.shop_user:
        if request.method=='POST':
            prod_name=request.POST['prod_name']
            prod_price=request.POST['prod_price']
            MRP=request.POST['mrp']
            prod_disc=request.POST['prod_disc']
            cate1=request.POST['cate']
            discount=round(((float(MRP)-float(prod_price))/float(MRP))*100,1)
            category=category_prod.objects.filter(shop=shop,name=cate1)[0]
            a.MRP=MRP
            a.discount=discount
            a.category_n=category
            a.prod_name=prod_name
            a.prod_price=prod_price
            a.prod_disc=prod_disc
            a.save()
        return redirect(f'/productupdate/{a.shop.id}')
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')


def delete_prod(request,prodid):

    a=products.objects.filter(id=prodid)
    
    if request.user==a[0].shop.shop_user:
        p=a[0].shop.id
        a.delete()
        return redirect(f'/productupdate/{p}')
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')
@login_required(login_url='/login')
def add_to_cart(request,prodid,cmd):
    if cmd=='add':
        a=products.objects.filter(id=prodid)[0]
        shopn=a.shop
        if request.method=="POST":
            quantity=request.POST['quantity']
        add=cart.objects.create(user=request.user,products=a,quantity=quantity,shop=shopn)
        add.save()
        return redirect(f'/shops/{a.shop.shop_id}')
    if cmd=='delete':
        dele=cart.objects.filter(user=request.user,id=prodid)
        shop=dele[0].shop.shop_id
        dele.delete()
        messages.error(request, 'Product has been removed form cart succesfully')
        return redirect(f'/shops/{shop}')

@login_required(login_url='/login')
def order_cart(request,shopid):
    shopn=shop.objects.filter(id=shopid)[0]
    cart_chechkout=cart.objects.filter(user=request.user,shop=shopn)
    total_price=0
    for i in cart_chechkout:
        total_price+=i.products.prod_price
    int_hand_fee=round(total_price/100)
    tax=0
    total=total_price+tax+int_hand_fee
    data=''
    for item in cart_chechkout:
        data= data + item.products.prod_name + ','+ str(item.products.prod_price) + ',' + str(item.products.id) + ';'
    order_price=f'Total price:{total_price} InternetFee: {int_hand_fee} Tax : {tax} Final Price {total}'
    if request.method=="POST":
        full_name=request.POST['full_name']
        mobile=request.POST['mobile']
        address=request.POST['address']
        address2=request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        address=f'{full_name} {mobile} {address} {address2} {city} {state} {zip} '
        order_create=order.objects.create(user=request.user,shop=shopn,price=order_price,items=data,address=address,
        payment='COD')
        order_create.save()
        dele=cart.objects.filter(user=request.user,shop=shopn)
        for a in dele:
            a.delete()
        
        messages.error(request, f'Order Placed SuccessFully, Order ID is {order_create.id}')
        return redirect(f'/shopview/{shopn.id}')
    
    params={'checkout':cart_chechkout,'shop':shopn,'total_price':total_price,'int_hand_fee':int_hand_fee,
    'tax':tax,'total':total}
    return render(request,'order.html',params)
@login_required(login_url='/login')
def order_tracker(request):
    track=order.objects.filter(user=request.user)
    param={'order':track}
    return render(request,'order_tracker.html',param)

def orders_for_shop(request,shopid):
    shopn=shop.objects.filter(id=shopid)[0]
    if request.user==shopn.shop_user:
        shopn=shop.objects.filter(id=shopid)[0]
        track=order.objects.filter(shop=shopn)
        param={'order':track,'shop':shopn}
        return render(request,'orders_for_shop.html',param)
    
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')

def order_update(request,orderid):
    up=order.objects.filter(user=request.user,id=orderid)[0]
    if request.user==up.shop.shop_user:
        if request.method=="POST":
            status=request.POST['status']
            up.status=status
            up.save()
        return redirect(f'/orders/{up.shop.id}')
    else:
        messages.error(request, 'Login With Your Business Account')
        return redirect('/login')

def search(request):
    query=request.GET['search']
    if len(query)==0:
        data=shop.objects.none()
        prod=products.objects.none()
    else:
        data1=shop.objects.filter(shop_name__icontains=query)
        data2=shop.objects.filter(shop_disc__icontains=query)
        prod1=products.objects.filter(prod_name__icontains=query)
        prod2=products.objects.filter(prod_disc__icontains=query)
        prod=prod1.union(prod2)
        data=data1.union(data2)
    param={'data':data,'query':query,'prod':prod}
    return render(request,'search.html',param)

def contact_us(request):
    if request.method=='POST':
        email=request.POST['email']
        sub=request.POST['subject']
        msg=request.POST['msg']
        a=contact.objects.create(email=email,sub=sub,msg=msg)
        a.save()
        messages.success(request, 'Thanks for contacting us ! We will reach you soon')
        return redirect('/contact')
    return render(request,'contact_us.html')

def blog_home(request):
    post=myblog.objects.all()
    param={'blog':post}
    return render(request,'blog_home.html',param)
   

def blog_full(request,slug):
    post=myblog.objects.filter(slug=slug)[0]
    param={'blog':post}
    return render(request,'blog_full.html',param)
@login_required(login_url='/login')
def rate(request,id):
    shopn=shop.objects.filter(id=id)[0]
    rate_obj=rateing.objects.filter(shop=id)
    if request.method=='POST':
        rating=request.POST['rateinput']
        review=request.POST['review']
        a=rateing.objects.create(user=request.user,shop=shopn,rate=rating,review=review)
        a.save()
    return redirect(f'/shops/{shopn.shop_id}')

def all_review(request,id):
    shopn=shop.objects.filter(id=id)[0]
    rate_obj=rateing.objects.filter(shop=id)
    param={'rate':rate_obj,'shop':shopn}
    return render(request,'allreview.html',param)
    


@login_required(login_url='/login')
def rateprod1(request,id):
    prod=products.objects.filter(id=id)[0]
    if request.method=='POST':
        rating=request.POST['rateinput']
        review=request.POST['review']
        a=rateprod.objects.create(user=request.user,prod=prod,rate=rating,review=review)
        a.save()
        messages.success(request, f'Thanks for your feedback')
    return redirect(f'/full/{prod.slug}')
def all_prod_rev(request,slug):
    prod=products.objects.filter(slug=slug)[0]
    rate_obj=rateprod.objects.filter(prod=prod)
    isprod=True
    param={'rate':rate_obj,'prod':prod,'isprod':isprod}
    return render(request,'allreview.html',param)
def fullprod(request,slug):
    prod=products.objects.filter(slug=slug)[0]
    shopid=prod.shop.id
    rate=rateprod.objects.filter(prod=prod)
    avg=rateprod.objects.filter(prod=prod).aggregate(Avg('rate'))
    shopn=shop.objects.filter(id=shopid)[0]
    param={'prod':prod,'shop':shopn,'rate':rate}
    if avg['rate__avg'] is None:
        avg['rate__avg']=5
    prod.rating=round(avg['rate__avg'],1)
    prod.save()
    param['rate__avg']=round(avg['rate__avg'],1)
    if param['rate__avg']>=3.5:
        param['rate_col']='success'
    elif  param['rate__avg']>=2.5:
        param['rate_col']='warning'
    else:
        param['rate_col']='danger'
    
    return render(request,'product.html',param)

@login_required(login_url='/login')
def addcategory(request,com):
    if com=="add":
        if request.method=='POST':
            shop_id=request.POST['Shop_id']
            shop1=shop.objects.filter(shop_id=shop_id)[0]
            cat_name=request.POST['cat_name']
            a=category_prod.objects.create(shop=shop1,name=cat_name)
            a.save()
            messages.success(request, f'Category {cat_name} added')
    else:
        pass
    return redirect(f"/shops/{shop_id}")
    