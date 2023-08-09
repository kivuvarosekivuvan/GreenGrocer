from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm

def create_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payment_list")
    else:
        form = PaymentForm()
    return render(request, "payment/create_payment.html", {"form": form})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, "payment/payment_list.html", {"payments": payments})

def payment_detail(request, id):
    payment = get_object_or_404(Payment, id=id)
    return render(request, "payment/payment_detail.html", {"payment": payment})


def edit_payment(request, id):
    payment = get_object_or_404(Payment, id=id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_detail', id=id)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment/edit_payment.html', {'form': form, 'payment': payment})
