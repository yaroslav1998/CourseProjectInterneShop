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
    product = Product.objects.only('id').get(id=product_id)
    nmb=data.get("nmb")
    is_delete=data.get("is_delete")
    if is_delete =='true':
      product=ProductInBasket.objects.filter(id=product).update(is_active_basket=False)

    else:
        new_product,created=ProductInBasket.objects.get_or_create(session_key=session_key,product_id=product,is_active_basket=True,defaults={"count":nmb})
        if not created:
            new_product.count+=int(nmb)
            new_product.save(force_update=True)


    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active_basket=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"]=products_total_nmb
    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict=dict()
        product_dict["id"] = item.id
        product_dict["name"]=item.product_id.name

        product_dict["nmb"]=item.count
        product_dict["total_price"] = item.Full_price
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    products_in_basket=ProductInBasket.objects.filter(session_key=session_key,is_active_basket=True)
    return  render(request,'checkout.html',locals())
