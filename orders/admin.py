from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    class Meta:
        model=Order
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
    class Meta:
        model=OrderItem
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)