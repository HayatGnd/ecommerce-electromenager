from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/',include('products.urls')), #on dit que toutes les urls qui commencent par api/ vont etre traitées par products.urls
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #pour que django serve les images