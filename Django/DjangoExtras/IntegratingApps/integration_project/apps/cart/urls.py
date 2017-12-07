from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process_order$', views.process_order, name="process"),
    url(r'^checkout$', views.checkout, name="checkout"),
    url(r'^clear$', views.clear, name="clear")
]
