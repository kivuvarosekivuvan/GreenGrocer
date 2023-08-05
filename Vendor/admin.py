from django.contrib import admin
from .models import Vendor

# Register your models here.
class Vendor_detail(admin.ModelAdmin):
    list_display = ("name", "email_address", "home_address")

admin.site.register(Vendor, Vendor_detail);    