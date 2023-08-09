from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Delivery
from .forms import DeliveryForm

def create_delivery(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("delivery_list")
    else:
        form = DeliveryForm()
    return render(request, "Delivery/create_delivery.html", {"form": form})

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, "Delivery/delivery_list.html", {"deliveries": deliveries})

def delivery_detail(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    return render(request, "Delivery/delivery_detail.html", {"delivery": delivery})

def edit_delivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    if request.method == "POST":
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect("delivery_detail", id=id)
    else:
        form = DeliveryForm(instance=delivery)
    return render(request, "Delivery/edit_delivery.html", {"form": form, "delivery": delivery})

def delete_delivery(request, id):
    delivery = get_object_or_404(Delivery, id=id)
    if request.method == "POST":
        delivery.delete()
        return redirect("delivery_list")
    return render(request, "Delivery/delete_delivery.html", {"delivery": delivery})
