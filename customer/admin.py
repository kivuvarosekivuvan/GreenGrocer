from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email_address", "home_address", "payment_method", "order_history", "rating")

admin.site.register(Customer, CustomerAdmin)    
