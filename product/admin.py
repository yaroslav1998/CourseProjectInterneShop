from django.contrib import admin
from .models import *

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer._meta.fields]
    class Meta:
        model=Manufacturer


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    class Meta:
        model=Product
class ProductRateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductRate._meta.fields]
    class Meta:
        model=ProductRate
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductReview._meta.fields]
    class Meta:
        model=ProductReview
class ProductSaleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductSale._meta.fields]
    class Meta:
        model=ProductSale

admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductRate,ProductRateAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(ProductSale,ProductSaleAdmin)