from django.urls import path
from . import views
from .views import customer_upload_view
from .views import customer_list
from .views import customer_detail
from .views import customer_detail_view
from .views import customer_delete



urlpatterns = [
    path('customer/upload', views.customer_upload_view, name="customer_upload_view"),
    path('customers/list', views.customer_list, name="customer_list_view"),
    path('customer/<int:id>/', views.customer_detail, name='customer_detail_view'),
    path('customers/edit/<int:id>/', views.customer_detail_view, name="customer_update_view"),
    path('customers/delete/<int:id>/', views.customer_delete, name="customer_delete_view"),
]
