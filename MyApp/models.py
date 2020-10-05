from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here. My Class model will be deleted
class shop(models.Model):
    shop_id=models.CharField(max_length=20,default='',unique=True)
    tophtml=models.CharField(max_length=2000,default='',blank=True)
    shop_name=models.CharField(max_length=500)
    shop_user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop_pic=models.ImageField(upload_to="media/")
    shop_disc=models.CharField(max_length=2000)
    shop_add=models.CharField(max_length=1000)
    verified=models.BooleanField(default=False)
    contact=models.IntegerField(default='')
    delivery=models.BooleanField(default=False)
    loclity=models.CharField(default='',max_length=50)
    clicks=models.IntegerField(default=0)
    city=models.CharField(default='Bareilly',max_length=50)
    rating=models.FloatField(default=5)
    live=models.BooleanField(default=False)
    Grocery = 'Grocery'
    Medical = 'Medical'
    DailyE='DailyE'
    Mobile="Mobile"
    electronics="electronics"
    clothing="clothing"
    food="food"
    furtunier="furtunier"
    gifts="gifts"
    computers="computers"
    jewellery="jewellery"
    book="book"
    Stationery="Stationery"


    CHOICES = [
        (Grocery, 'Grocery'),
        (Medical, 'Medical'),
        (DailyE, 'DailyE'),(Mobile,"Mobile"),(electronics,"electronics"),(clothing,"clothing"),(food,"food"),(furtunier,"furtunier"),
        (gifts,"gifts"),(computers,"computers"), (jewellery,"jewellery"),(book,"book"),(Stationery,"Stationery")]
    category = models.CharField(max_length=20,choices=CHOICES,default=Grocery)
    bottomhtml=models.CharField(max_length=2000,default='',blank=True)
    def __str__(self):
        return self.shop_name
    
class category_prod(models.Model):
    name=models.CharField(default=" ",max_length=100)
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)
    def __str__(self):
        return self.shop.shop_name + ' - ' + self.name

class products(models.Model):
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=2000,blank=True,unique=True)
    prod_name=models.CharField(max_length=500)
    prod_disc=models.CharField(max_length=500)
    prod_price=models.FloatField()
    MRP=models.FloatField(blank=True)
    discount=models.FloatField(blank=True)
    rating=models.FloatField(default=5)
    about=RichTextUploadingField(blank=True)
    category_n = models.ForeignKey(category_prod,on_delete=models.CASCADE,blank=True, null=True)
    review=models.BooleanField(default=False)
    affiliate=models.BooleanField(default=False)
    affiliate_link=models.CharField(max_length=500,blank=True)
    affiliate_img=models.CharField(max_length=500,blank=True)
    prod_img=models.ImageField(upload_to="media/")

    def __str__(self):
        return self.prod_name + ' by ' + self.shop.shop_name
def sluf_gen(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.prod_name)
pre_save.connect(sluf_gen,sender=products)

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    products=models.ForeignKey(products,on_delete=models.CASCADE)
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


    
class order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)
    price=models.CharField(max_length=100)
    items=models.CharField(max_length=2000)
    date=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=1000)
    Pending = 'Pending'
    Accepted = 'Accepted'
    Dispatched='Dispatched'
    Denied='Denied'
    Delivered='Delivered'
    COD='COD'
    Online='Online'
    CHOICES = [
        (Pending, 'Pending'),
        (Accepted, 'Accepted'),
        (Dispatched, 'Dispatched'),
        (Denied, 'Denied'),
        (Delivered, 'Delivered')]
    status = models.CharField(max_length=20,choices=CHOICES,default=Pending)
    Mode=[
        (COD,'COD'),
        (Online,'Online')
    ]
    payment = models.CharField(max_length=20,choices=Mode,default=COD)

    def __str__(self):
        return self.user.username
    
    
class contact(models.Model):
    email=models.CharField(max_length=100)
    sub=models.CharField(max_length=100,blank=True)
    msg=models.TextField(max_length=None)

class myblog(models.Model):
    title=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    content=RichTextUploadingField()
    slug=models.SlugField(max_length=1000,unique=True)
    def __str__(self):
        return self.title
pre_save.connect(sluf_gen,sender=myblog)
class rateing(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)
    rate=models.IntegerField(choices= [(i,i) for i in range(1,6)])
    review=models.TextField(blank=True)

class rateprod(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prod=models.ForeignKey(products,on_delete=models.CASCADE)
    rate=models.IntegerField(choices= [(i,i) for i in range(1,6)])
    review=models.TextField(blank=True)
    
