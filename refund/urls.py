from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_refund, name="create_refund"),
    path("list/", views.refund_list, name="refund_list"),
    path("<int:id>/", views.refund_detail, name="refund_detail"),
    path("<int:id>/edit/", views.edit_refund, name="edit_refund"),
    path("<int:id>/delete/", views.delete_refund, name="delete_refund"),
]
