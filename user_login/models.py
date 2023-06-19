from django.db import models

# Create your models here.
class User_Login(models.Model):
    user_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number =models.CharField(max_length=32)
    date_of_birth = models.DateTimeField()