from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    # user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/')
    name=models.CharField(max_length=32)
    email_address=models.EmailField()
    phone_number=models.CharField(max_length=32)
    home_address=models.CharField(max_length=32)
    order_history= models.JSONField()
    payment_method=models.CharField(max_length=32)
    rating=models.FloatField()

class Meta:
        verbose_name_plural = "customer"