from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
    path('reviews/create/', views.create_review, name='create_review'),
]
