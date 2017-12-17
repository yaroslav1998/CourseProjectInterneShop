from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from product.models import *
from django.shortcuts import get_object_or_404

def basket_adding(request):
    return_dict=dict()
    session_key = request.session.session_key
    print(request.POST)
    data=request.POST
    product_id=data.get("product_id")
    nmb=data.get("nmb")
    product=Product.objects.only('id').get(id=product_id)

    new_product,created=ProductInBasket.objects.get_or_create(session_key=session_key,product_id=product,count=nmb)
    products_total_nmb=ProductInBasket.objects.filter(session_key=session_key,product_id=product_id,is_active_basket=True).count()
    #data=request.POST
    #product_id=data.get("product_id")
    #nmb=data.get("nmb")

   # new_product=ProductInBasket.objects.create(session_key=session_key,product_id=product_id,count=nmb)
    #product_total_nmb=ProductInBasket.objects.filter(session_key=session_key,is_active_basket=True).count()
    return_dict["products_total_nmb"]=products_total_nmb
    return JsonResponse(return_dict)