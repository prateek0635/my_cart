from django.contrib import admin
from .models import shop,products,cart,order

# Register your models here.
admin.site.register(shop)
admin.site.register(products)
admin.site.register(cart)
admin.site.register(order)


