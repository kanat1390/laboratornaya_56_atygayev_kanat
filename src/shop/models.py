from random import choices
from django.db import models
from django.urls import reverse
from .managers import ProductManager

CATEGORY_CHOICES = (
    ('other', 'Разное'),
    ('tv','Телевизоры'),
    ('smartphone','Смартфоны'),
)


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=True, blank=True, max_length=2000)
    image = models.ImageField(null=True, blank=True, upload_to='products/images/')
    category = models.CharField(choices=CATEGORY_CHOICES, null=False, blank=False, default='other', max_length=100)
    qty = models.PositiveIntegerField(default=0, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    objects = ProductManager()

    def display_price(self):
        return f'{self.price}$'
    
    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk':self.id})

    def get_category_url(self):
        return reverse('product-by-category', kwargs={'category':self.category})

    def __str__(self):
        return self.name


