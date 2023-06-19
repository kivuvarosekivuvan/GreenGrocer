from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display =("payment_method", "amount", "currency", "date_of_payment", "status")

admin.site.register(Payment, PaymentAdmin)