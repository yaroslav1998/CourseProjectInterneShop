from django.shortcuts import render
from product.models import *
from category.models import *

def home(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main=True,product__is_active=True)
    categoryes=Category.objects
    return render(request,'landing/Home.html',locals())