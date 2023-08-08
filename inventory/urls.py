from django.urls import path
from .views import product_upload_view
from .views import product_list
from .views import product_detail_view
from .import views



urlpatterns=[
    path('products/upload' , views.product_upload_view,name ="product_upload_view"),
    path("products/list", views.product_list, name = "product_list_view"),
    path('product/<int:id>/', views.product_detail, name='product_detail_view'),
    path('products/edit/<int:id>/', views.product_detail_view, name="product_update_view"),
    path('products/delete/<int:id/', views.product_delete, name="product_delete_view")


    
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)