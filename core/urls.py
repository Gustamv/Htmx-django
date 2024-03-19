from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #3- adding path and importing including the urls.py
    path('', include('products.urls'))
]
