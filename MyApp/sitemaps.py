from django.contrib.sitemaps import Sitemap
from .models import products,shop
from django.urls import reverse
from MyApp import views
 
class ProdSitemap(Sitemap):    
    changefreq = "daily"
    priority = 1.0
 
    def items(self):
        return products.objects.all()
    def location(self, item):
        return reverse('fullprod', args=[str(item.slug)])
    