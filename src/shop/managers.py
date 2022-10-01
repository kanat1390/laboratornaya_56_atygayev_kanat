from django.db import models

class ProductManager(models.Manager):
    def in_stock(self):
        return self.filter(qty__gt=0)