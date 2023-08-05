from django.db import models
from customer.models import Customer
from product_cart.models import Product_Cart
from delivery.models import Delivery

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product_cart= models.ForeignKey(Product_Cart, null=True, on_delete=models.CASCADE)
    delivery= models.OneToOneField(Delivery, null=True, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=32)
    order_date= models.DateTimeField()
    total_amount=models.IntegerField()
    delivery_address=models.CharField(max_length=32)
    contact_number=models.CharField(max_length=32)
    payment_status=models.BooleanField()

    order_status=models.BooleanField()
    payment_method=models.CharField(max_length=32)

class Meta:
        verbose_name_plural = "order"