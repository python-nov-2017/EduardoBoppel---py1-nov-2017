from django.contrib import admin
from .models import Manufacturer, Product


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'email', 'phone', 'website')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'manufacturer', 'price', 'on_stock', 'is_active')


