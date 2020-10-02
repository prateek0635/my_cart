from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve 
from django.contrib.sitemaps.views import sitemap
from MyApp.sitemaps import ProdSitemap

sitemaps={
    'prods':ProdSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyApp.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
