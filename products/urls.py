#4- importing paths and creating a url pattern list products
from django.urls import path
#5- import views #14 import htmx_views
from . import views, htmx_views


urlpatterns = [
    #adding / after list_products
    path('list_products/', views.list_products, name='list_products')
]

#11- create a view that will receive the inputs and save
#11.1- creating a var to store htmx urls

htmx_urlpatterns = [
    path('check_product/', htmx_views.check_product, name='check_product'),
    #20- create e new path for a save_product template, then go to view and create it
    path('save_product/', htmx_views.save_product,name='save_product')
    ]

#15- in order to django recognize htmx_urlpatterns, we must do it
urlpatterns += htmx_urlpatterns
