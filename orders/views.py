from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404

def basket_adding(request):
    return_dict=dict()
    session_key = request.session.session_key
    print(request.POST)
    data=request.POST
    product_id=data.get("product_id")
    new_product=ProductInBasket.objects.get(product_id=product_id)
    #get_object_or_404(ProductInBasket, session_key=session_key)
    #data=request.POST
    #product_id=data.get("product_id")
    #nmb=data.get("nmb")

   # new_product=ProductInBasket.objects.create(session_key=session_key,product_id=product_id,count=nmb)
    #product_total_nmb=ProductInBasket.objects.filter(session_key=session_key,is_active_basket=True).count()
    #return_dict["product_total_nmb"]=product_total_nmb
    return JsonResponse(return_dict)