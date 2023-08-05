from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=32)
    email_address=models.EmailField()
    phone_number=models.CharField(max_length=32)
    home_address=models.CharField(max_length=32)
   

class Meta:
        verbose_name_plural = "vendor"
