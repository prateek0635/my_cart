from django.contrib import admin
from .models import shop,products,cart,order,contact,myblog

# Register your models here.
admin.site.register(shop)
admin.site.register(products)
admin.site.register(cart)
admin.site.register(order)
admin.site.register(contact)
admin.site.register(myblog)

