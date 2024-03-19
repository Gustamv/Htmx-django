from django.shortcuts import render
from .models import Product

# Create your views here.
#6- create a function for list_products

def list_products(request):
    #24- import this from .models import Product and add the product = Product.objects.all() in order to fetch all the products listed
    products = Product.objects.all()
    #25 add {'products': products}
    return render(request, 'list_products.html', {'products': products})
