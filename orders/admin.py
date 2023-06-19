from django.contrib import admin
from .models import Order

# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display =("customer_name", "order_date", "total_amount", "delivery_address", "contact_number", "payment_status", "order_status", "payment_method")

admin.site.register(Order, OrdersAdmin)