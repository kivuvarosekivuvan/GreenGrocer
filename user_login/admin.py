from django.contrib import admin
from .models import User_Login
# Register your models here.


class UserloginAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email", "password", "first_name", "last_name", "phone_number", "date_of_birth")

admin.site.register(User_Login, UserloginAdmin)