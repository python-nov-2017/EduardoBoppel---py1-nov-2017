from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^addcourse$', views.addcourse, name="addcourse"),
    url(r'^createcourse$', views.createcourse, name="createcourse"),
    url(r'^(?P<id>\d+)/editcourse$', views.editcourse, name="editcourse"),
    url(r'^(?P<id>\d+)/updatecourse$', views.createcourse, name="updatecourse"),
    url(r'^(?P<id>\d+)/deletecourse$', views.deletecourse, name="deletecourse"),
    url(r'^(?P<id>\d+)/showcomments$', views.showcomments, name="showcomments"),
    url(r'^(?P<id>\d+)/addcomment$', views.addcomment, name="addcomment"),

]
