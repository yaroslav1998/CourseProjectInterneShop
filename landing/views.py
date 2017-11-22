from django.shortcuts import render
from product.models import *
from category.models import *

def home(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main=True,product__is_active=True)
    category=Category.objects.all()
    return render(request,'landing/Home.html',locals())