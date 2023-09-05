from django.urls import path
from . import views

urlpatterns = [
    path('vendors/upload/', views.vendor_upload_view, name="vendor_upload_view"),
    path('vendors/list/', views.vendor_list, name="vendor_list_view"),
    path('vendor/<int:id>/', views.vendor_detail, name='vendor_detail_view'),
    path('vendors/edit/<int:id>/', views.vendor_edit, name="vendor_edit_view"),
    path('vendors/delete/<int:id>/', views.vendor_delete, name="vendor_delete_view"),
]
