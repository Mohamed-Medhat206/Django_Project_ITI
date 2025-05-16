from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('name', 'description', 'sku')
    prepopulated_fields = {'slug': ('name',)}