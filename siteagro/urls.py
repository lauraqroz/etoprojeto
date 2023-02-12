from principal.views import *
from django.contrib import admin
from principal.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from siteagro import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_index),
    path('inicio', index, name = 'index'),
    path('mercadoria/', mercadoria, name= 'mercadoria'),
    path('about/', about, name='about'),
    path('add/', add , name='add'),
    path('', include ('usuarios.urls')),
    

]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
