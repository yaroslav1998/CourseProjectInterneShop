from django.contrib import admin
from Data.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    class Meta:
        model=User
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    class Meta:
        model=Category
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Manufacturer._meta.fields]
    class Meta:
        model=Manufacturer
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    class Meta:
        model=Order
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
    class Meta:
        model=OrderItem
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
class StockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stock._meta.fields]
    class Meta:
        model=Stock
class ProductStockBalanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductStockBalance._meta.fields]
    class Meta:
        model=ProductStockBalance
admin.site.register(Category,CategoryAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductRate,ProductRateAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(ProductSale,ProductSaleAdmin)
admin.site.register(Stock,StockAdmin)
admin.site.register(ProductStockBalance,ProductStockBalanceAdmin)
admin.site.register(User,UserAdmin)