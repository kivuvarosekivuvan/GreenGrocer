from django.db import models

# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=32)
    store_location = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    contact_information = models.CharField(max_length=32)
    email = models.EmailField()

class Meta:
        verbose_name_plural = "store"