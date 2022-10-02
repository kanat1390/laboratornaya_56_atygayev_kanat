from ..models import Product
from django.shortcuts import get_object_or_404
from django.db.models.functions import Lower

def get_product_list():
    product_list = Product.objects.in_stock().order_by('category',Lower('name'))
    return product_list

def get_product_by_pk(pk):
    return get_object_or_404(Product, pk=pk)

def get_product_list_by_category(category):
    return Product.objects.in_stock().filter(category=category).order_by(Lower('name'))
