from django.db import models

class Payment(models.Model):
    payment_method= models.CharField(max_length=32)
    amount= models.DecimalField(decimal_places=4, max_digits=4)
    currency=models.DecimalField(decimal_places=4, max_digits=4)
    date_of_payment=models.DateTimeField()
    status=models.CharField(max_length=32)