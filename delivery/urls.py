from django.urls import path
from . import views

urlpatterns = [
    path('delivery/upload', views.create_delivery, name="create_delivery"),
    path('delivery/list', views.delivery_list, name="delivery_list"),
    path('delivery/<int:id>/', views.delivery_detail, name='delivery_detail'),
    path('delivery/edit/<int:id>/', views.edit_delivery, name="edit_delivery"),
    path('delivery/delete/<int:id>/', views.delete_delivery, name="delete_delivery"),
]
