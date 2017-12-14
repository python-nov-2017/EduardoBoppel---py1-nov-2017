from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Manufacturer, Product


class HomePageView(TemplateView):
    template_name = 'store/home.html'


class ManufacturerList(ListView):
    model = Manufacturer
    context_object_name = 'manufacturers'

class ManufacturerDetail(DetailView):
    model = Manufacturer
    context_object_name = 'manufacturer'

class ManufacturerCreate(CreateView):
    model = Manufacturer
    fields = ['name', 'address', 'city','country','phone', 'email', 'website']

class ManufacturerUpdate(UpdateView):
    model = Manufacturer
    fields = ['name', 'address', 'city','country','phone', 'email', 'website']

class ManufacturerDelete(DeleteView):
    model = Manufacturer
    template_name = 'store/confirm_delete.html'
    success_url = reverse_lazy('store:manufacturer_list')
    


#PRODUCTS
class ProductList(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'

class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'description', 'manufacturer', 'price', 'on_stock', 'is_active']

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'manufacturer', 'price', 'on_stock', 'is_active']

class ProductDelete(DeleteView):
    model = Product
    template_name = 'store/confirm_delete.html'
    success_url = reverse_lazy('store:product_list')