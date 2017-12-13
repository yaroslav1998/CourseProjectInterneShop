
from django.shortcuts import render
from product.models import *

def product(request,product_id):
    product=Product.objects.get(id=product_id)
    product_image=ProductImage.objects.filter(product_id=product_id)

    session_key=request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'Product.html', locals())