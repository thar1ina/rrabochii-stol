from django.shortcuts import render
from Shop.models import Product



def home(request):
    products = Product.object.filter(True)
    return  render(request, 'index.html', {'product': products})

