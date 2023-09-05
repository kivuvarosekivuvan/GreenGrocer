from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import ProductListView
from .views import ProductDetailView
from .views import OrderListView
from .views import OrderDetailView
from .views import CartListView
from .views import CartDetailView





urlpatterns=[
        path('customers/list', CustomerListView.as_view(), name="customer_list_view"),
        path('customers/<int:id>', CustomerDetailView.as_view(), name="customer_detail_view"),
        path("inventory/",ProductListView.as_view(),name="product_list_view"),
        path("inventory/<int:id>/",ProductDetailView.as_view(),name="product_detail_view"),
        path("order/",OrderListView.as_view(),name="order_list_view"),
        path("order/<int:id>/",OrderDetailView.as_view(),name="order_detail_view"),
        path("cart/",CartListView.as_view(),name="cart_list_view"),
        path("cart/<int:id>/",CartDetailView.as_view(),name="cart_detail_view"),


]