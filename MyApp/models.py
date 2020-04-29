from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here. My Class model will be deleted
class shop(models.Model):
    shop_id=models.CharField(max_length=20,default='',unique=True)
    shop_name=models.CharField(max_length=20)
    shop_user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop_pic=models.ImageField(upload_to="static/")
    shop_disc=models.CharField(max_length=100)
    shop_add=models.CharField(max_length=50)
    verified=models.BooleanField(default=False)
    contact=models.IntegerField(default='')
    delivery=models.BooleanField(default=False)
    Grocery = 'Grocery'
    Medical = 'Medical'
    DailyE='DailyE'


    CHOICES = [
        (Grocery, 'Grocery'),
        (Medical, 'Medical'),
        (DailyE, 'DailyE')]
    category = models.CharField(max_length=20,choices=CHOICES,default=Grocery)
    def __str__(self):
        return self.shop_name
    

class products(models.Model):
    shop=models.ForeignKey(shop,on_delete=models.CASCADE)
    prod_name=models.CharField(max_length=20)
    prod_disc=models.CharField(max_length=100)
    prod_price=models.FloatField()
    Grocery = 'Grocery'
    Medical = 'Medical'
    DailyE='DailyE'
    CHOICES = [
        (Grocery, 'Grocery'),
        (Medical, 'Medical'),
        (DailyE, 'DailyE')]
    category = models.CharField(max_length=20,choices=CHOICES,default=Grocery)
    prod_img=models.ImageField(upload_to="static/")

    def __str__(self):
        return self.prod_name + ' by ' + self.shop.shop_name
    
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
    items=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=200)
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
    email=models.CharField(max_length=30)
    sub=models.CharField(max_length=30,blank=True)
    msg=models.TextField(max_length=None)