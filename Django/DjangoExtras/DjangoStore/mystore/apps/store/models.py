from __future__ import unicode_literals
from django.urls import reverse
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=False)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, blank=False)
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:manufacturer_detail', kwargs={'pk': self.pk})

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, related_name="products")
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    on_stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'pk': self.pk})