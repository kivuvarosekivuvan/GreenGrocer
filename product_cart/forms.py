from django import forms
from .models import Product_Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Product_Cart
        fields = ['product_quantity', 'date_added']  # Adjust these fields as needed
