from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^createcourse$', views.createcourse),
    url(r'^(?P<id>\d+)/editcourse$', views.editcourse),
    url(r'^(?P<id>\d+)/updatecourse$', views.createcourse),
    url(r'^(?P<id>\d+)/deletecourse$', views.deletecourse),
    url(r'^(?P<id>\d+)/showcomments$', views.showcomments),
    url(r'^(?P<id>\d+)/addcomment$', views.addcomment),

    #USERS
    url(r'^users/$', views.users),
    url(r'^users/adduser$', views.adduser),
    url(r'^users/createuser$', views.updateuser),
    url(r'^users/(?P<id>\d+)/$', views.showuser),
    url(r'^users/(?P<id>\d+)/update$', views.updateuser),
    url(r'^users/(?P<id>\d+)/edit$', views.edituser),
    url(r'^users/(?P<id>\d+)/delete$', views.deleteuser),
]
