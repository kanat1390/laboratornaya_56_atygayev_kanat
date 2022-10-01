from django.shortcuts import render
from .services import product_services


def product_list_view(request):
    product_list = product_services.get_product_list()
    context = {
        'product_list': product_list,
    }
    return render(request, 'shop/product_list.html', context)

def product_detail_view(request, pk):
    product = product_services.get_product_by_pk(pk)
    context = {
        'product':product,
    }
    return render(request, 'shop/product_detail.html', context)


