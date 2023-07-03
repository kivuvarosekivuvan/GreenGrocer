from django.contrib import admin
from .models import Store
# Register your models here.

class Store_admin(admin.ModelAdmin):
    list_display = ("store_name","store_location", "address", "contact_information", "email")
admin.site.register(Store, Store_admin)