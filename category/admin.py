from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
    class Meta:
        model=Category

admin.site.register(Category,CategoryAdmin)