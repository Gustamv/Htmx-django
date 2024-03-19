from django.http import HttpResponse
from .models import Product
from django.shortcuts import render


#12- creating this archive
#def check_product(request):
#    product = request.GET.get('product')
#    print(product)
#    return HttpResponse('teste')

#17- updating the funtion in order to
def check_product(request):
    product = request.GET.get('product')
    products = Product.objects.filter(name=product)
    return render(request, 'partials/htmx_components/check_product.html', {'products': products})

#21- create a function for save_product
def save_product(request):
    name = request.POST.get('product')
    price = request.POST.get('price')

    product = Product(
        name=name,
        price=price
    )
    product.save()
    products = Product.objects.all()

    # this previous return worked!
    #return HttpResponse('palavras')
    #27- you must write on the render contest to show the products "{'products', products}"
    return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})
