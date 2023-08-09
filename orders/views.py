from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer_name = order.customer.name
            order.total_amount = order.product_cart.total_price
            order.delivery_address = order.delivery.address
            order.contact_number = order.customer.contact_number
            order.payment_status = False  
            order.order_status = False 
            order.save()
            return redirect("order_detail", id=order.id)
    else:
        form = OrderForm()
    return render(request, "order/create_order.html", {"form": form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, "order/order_list.html", {"orders": orders})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, "order/order_detail.html", {"order": order})


def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        order.delete()
        return redirect("order_list")
    return render(request, "order/delete_order.html", {"order": order})


def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_detail", id=id)
    else:
        form = OrderForm(instance=order)
    return render(request, "order/edit_order.html", {"form": form, "order": order})