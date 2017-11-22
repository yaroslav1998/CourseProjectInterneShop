from django.shortcuts import render

from django.shortcuts import render
from category.models import *
from product.models import *
def category(request,category_id):
  category=Category.objects.get(id=category_id)
  product=Product.objects.filter(category_id=category_id)
  return render(request,'Category.html',locals())