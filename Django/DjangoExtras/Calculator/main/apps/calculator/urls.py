from django.conf.urls import url
from .views import Calculator

urlpatterns = [
    url(r'^$', Calculator.as_view(), name="calculator"),

]
