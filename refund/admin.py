from django.contrib import admin
from .models import Refund
# Register your models here.

class Refund_Admin(admin.ModelAdmin):
    list_display = ("item_ordered", "requested_time", "reason", "approval")

admin.site.register(Refund, Refund_Admin)
