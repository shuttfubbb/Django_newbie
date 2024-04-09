from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('product.urls')),
    path('', include('cart.urls')),
    path('', include('search.urls')),
    path('admin/', admin.site.urls),
]
