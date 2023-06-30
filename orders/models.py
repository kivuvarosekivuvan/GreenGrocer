from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=32)
    order_date= models.DateTimeField()
    total_amount=models.IntegerField()
    delivery_address=models.CharField(max_length=32)
    contact_number=models.CharField(max_length=32)
    payment_status=models.BooleanField()
    # items=models.JSONField()
    order_status=models.BooleanField()
    payment_method=models.CharField(max_length=32)