from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra=0
class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra=0
class ProductRateInline(admin.TabularInline):
    model = ProductRate
    extra=0

class ProductInline(admin.TabularInline):
    model = Product
    extra=0
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,ProductReviewInline,ProductRateInline]
    class Meta:
        model=Product

admin.site.register(Product,ProductAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer._meta.fields]
    inlines = [ProductInline]
    class Meta:
        model=Manufacturer

admin.site.register(Manufacturer,ManufacturerAdmin)

class ProductRateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductRate._meta.fields]
    class Meta:
        model=ProductRate

admin.site.register(ProductRate,ProductRateAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductReview._meta.fields]
    class Meta:
        model=ProductReview

admin.site.register(ProductReview,ProductReviewAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    class Meta:
        model=ProductImage

admin.site.register(ProductImage,ProductImageAdmin)






