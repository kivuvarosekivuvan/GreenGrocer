from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_payment, name='create_payment'),
    path('list/', views.payment_list, name='payment_list'),
    path('<int:id>/', views.payment_detail, name='payment_detail'),
    path('<int:id>/edit/', views.edit_payment, name='edit_payment'), 
]
