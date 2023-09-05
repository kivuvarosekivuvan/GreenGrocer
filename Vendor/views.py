from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendor
from .forms import VendorForm

def vendor_upload_view(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list_view')  # Redirect to the vendor list after successful upload
    else:
        form = VendorForm()
    return render(request, 'Vendor/vendor_upload.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'Vendor/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    return render(request, 'Vendor/vendor_detail.html', {'vendor': vendor})

def vendor_edit(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_detail_view', id=vendor.id)
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'Vendor/vendor_edit.html', {'form': form})

def vendor_delete(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list_view')
    return render(request, 'Vendor/vendor_delete.html', {'vendor': vendor})
