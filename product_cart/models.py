from django.db import models
from inventory.models import Product


# Create your models here.
class Product_Cart(models.Model):
    products= models.ManyToManyField(Product)
    
    product_name = models.CharField(max_length=32)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_image =models.ImageField()
    date_added = models.DateTimeField()

class Meta:
        verbose_name_plural = "cart"