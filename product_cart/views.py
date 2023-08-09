from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product_Cart
from inventory.models import Product  
from .forms import CartForm  

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.product_name = product.name
            cart_item.product_price = product.price
            cart_item.product_image = product.image
            cart_item.save()
            return redirect("cart")
    else:
        form = CartForm()
    return render(request, "cart/add_to_cart.html", {"form": form, "product": product})


def cart(request):
    cart_items = Product_Cart.objects.all()
    for cart_item in cart_items:
        cart_item.total_price = cart_item.product_price * cart_item.product_quantity
    return render(request, "cart/cart.html", {"cart_items": cart_items})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Product_Cart, id=cart_item_id)
    if request.method == "POST":
        cart_item.delete()
        return redirect("cart")
    return render(request, "cart/remove_from_cart.html", {"cart_item": cart_item})
