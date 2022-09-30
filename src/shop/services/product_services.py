from ..models import Product

def get_product_list():
    product_list = Product.objects.all()
    return product_list