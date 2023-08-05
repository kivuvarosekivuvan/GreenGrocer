

from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product
from django.shortcuts import render,redirect

def product_upload_view(request):
    if request.method == "POST":
        form = ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()


    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form": form})

def product_list(request):         
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})
    # you can add processing bar or any further logic if needed


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, "inventory/product_detail.html", {"product": product})

def product_detail_view(request, id):        
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=id)
    else:
        form = ProductUploadForm(instance=product)
    return render(request, "inventory/edit_product.html", {"form": form})

def product_delete(request,id):
    product= Product.objects.get(id=id)
    product.delete()
    return render("product_delete_view", id=id)
