from django.conf.urls import url
from . import views
from .views import HomePageView, ManufacturerList, ManufacturerDetail, ManufacturerCreate, ManufacturerUpdate, ManufacturerDelete, ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="index"),

    url(r'^manufacturer/$', ManufacturerList.as_view(), name="manufacturer_list"),
    url(r'^manufacturer/add/$', ManufacturerCreate.as_view(), name="manufacturer_add"),
    url(r'^manufacturer/(?P<pk>\d)/$', ManufacturerDetail.as_view(), name="manufacturer_detail"),
    url(r'^manufacturer/(?P<pk>\d)/edit$', ManufacturerUpdate.as_view(), name="manufacturer_update"),
    url(r'^manufacturer/(?P<pk>\d)/delete/$', ManufacturerDelete.as_view(), name="manufacturer_delete"),

    url(r'^product/$', ProductList.as_view(), name="product_list"),
    url(r'^product/add/$', ProductCreate.as_view(), name="product_add"),
    url(r'^product/(?P<pk>\d)/$', ProductDetail.as_view(), name="product_detail"),
    url(r'^product/(?P<pk>\d)/edit$', ProductUpdate.as_view(), name="product_update"),
    url(r'^product/(?P<pk>\d)/delete/$', ProductDelete.as_view(), name="product_delete"),


]
