from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product_cart', 'delivery', 'customer_name', 'order_date', 'total_amount', 'delivery_address', 'contact_number', 'payment_status', 'order_status', 'payment_method']
