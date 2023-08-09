from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('list/', views.order_list, name='order_list'),
    path('<int:id>/', views.order_detail, name='order_detail'),
    path('edit/<int:id>/', views.edit_order, name='edit_order'),
    path('delete/<int:id>/', views.delete_order, name='delete_order'),
]
