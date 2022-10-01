from django.shortcuts import render, redirect
from .services import product_services
from .forms import ProductModelForm
from django.urls import reverse

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

def product_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        product = form.save()
        return redirect(reverse('product-detail', kwargs={'pk': product.id}))
    context = {
        'form': form,
    }
    return render(request, 'shop/product_create.html', context)




