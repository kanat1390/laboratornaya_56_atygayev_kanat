from django.urls import path
from .views import (
    product_list_view,
    product_detail_view
)
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('products/<int:pk>/', product_detail_view, name='product-detail'),
]
