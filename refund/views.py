from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Refund
from .forms import RefundForm

def create_refund(request):
    if request.method == "POST":
        form = RefundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("refund_list")
    else:
        form = RefundForm()
    return render(request, "refund/create_refund.html", {"form": form})

def refund_list(request):
    refunds = Refund.objects.all()
    return render(request, "refund/refund_list.html", {"refunds": refunds})

def refund_detail(request, id):
    refund = get_object_or_404(Refund, id=id)
    return render(request, "refund/refund_detail.html", {"refund": refund})

def edit_refund(request, id):
    refund = get_object_or_404(Refund, id=id)
    if request.method == "POST":
        form = RefundForm(request.POST, instance=refund)
        if form.is_valid():
            form.save()
            return redirect("refund_detail", id=id)
    else:
        form = RefundForm(instance=refund)
    return render(request, "refund/edit_refund.html", {"form": form, "refund": refund})

def delete_refund(request, id):
    refund = get_object_or_404(Refund, id=id)
    if request.method == "POST":
        refund.delete()
        return redirect("refund_list")
    return render(request, "refund/delete_refund.html", {"refund": refund})
