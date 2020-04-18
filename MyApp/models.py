from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here. My Class model will be deleted
class myclass(models.Model):
    id=models.AutoField(primary_key=True)
    titel=models.CharField(max_length=100)
    data=models.DateField()
    disc=models.CharField(max_length=1000)
    pic=models.ImageField(upload_to="static/")
    Grocery = 'Grocery'
    Medical = 'Medical'
    DailyE='DailyE'
    CHOICES = [
        (Grocery, 'Grocery'),
        (Medical, 'Medical'),
        (DailyE, 'DailyE')]
    category = models.CharField(max_length=20,choices=CHOICES,default=Grocery,)


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
    


class oredr(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    prod_name=models.CharField(max_length=30) 
    price=models.IntegerField(default='0')
    quantity=models.CharField(max_length=10,default='')

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
        return self.prod_name
    
