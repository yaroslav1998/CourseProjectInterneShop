from django.contrib import admin
from .models import *

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    class Meta:
        model=Order
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]
    class Meta:
        model=OrderItem
class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    class Meta:
        model=Status
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Status,StatusAdmin)