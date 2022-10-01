from django.urls import path
from .views import (
    product_list_view,
    product_detail_view,
    product_create_view,
    product_update_view,
    product_delete_view,
    product_delete_confirm_view,
)
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('products/<int:pk>/', product_detail_view, name='product-detail'),
    path('products/create/', product_create_view, name='product-create'),
    path('products/<int:pk>/update/', product_update_view, name='product-update'),
    path('products/<int:pk>/delete/', product_delete_view, name='product-delete'),
    path('products/<int:pk>/delete/confirm/', product_delete_confirm_view, name='product-delete-confirm'),
]
