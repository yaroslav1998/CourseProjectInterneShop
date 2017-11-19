from django.shortcuts import render
from product.models import  Product

def landing(request):
    return  render(request,'HomePage.html',locals())
def home(request):
    products = Product.objects.filter(is_active=True)

    return  render(request,'landing/Home.html',locals())