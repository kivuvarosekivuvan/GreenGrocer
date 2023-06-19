from django.contrib import admin
from .models import Product_Cart

# Register your models here.
class Product_cartAdmin(admin.ModelAdmin):
    list_display=("product_name", "product_price", "product_quantity", "product_image", "date_added")

admin.site.register(Product_Cart, Product_cartAdmin)