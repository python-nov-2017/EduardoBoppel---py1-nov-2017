from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_note/$', views.add_note, name="add_note"),
    url(r'^add_description/(?P<id>\d+)/$', views.add_description, name="add_description"),
    url(r'^delete_note/(?P<id>\d+)/$', views.delete_note, name="delete_note"),
]
