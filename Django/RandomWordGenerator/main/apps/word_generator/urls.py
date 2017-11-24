from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate_number$', views.generate_number),
    url(r'^reset$', views.reset),
]