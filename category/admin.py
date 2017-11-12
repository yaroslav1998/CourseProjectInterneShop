from django.contrib import admin
from .models import *
from product.models import *
class ProductInline(admin.TabularInline):
    model = Product
    extra = 0
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    inlines = [ProductInline]
    class Meta:
        model=Category

admin.site.register(Category,CategoryAdmin)