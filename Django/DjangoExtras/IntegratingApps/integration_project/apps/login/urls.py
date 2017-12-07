from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home/$', views.home, name="home"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^registermodelform/$', views.registermodelform, name="register"),
    url(r'^loginnormalform/$', views.loginnormalform, name="login"),
    
    #USERS
    url(r'^users/$', views.users, name="users"),
    url(r'^users/adduser$', views.adduser, name="adduser"),
    url(r'^users/createuser$', views.updateuser, name="createuser"),
    url(r'^users/(?P<id>\d+)/$', views.showuser, name="showuser"),
    url(r'^users/(?P<id>\d+)/update$', views.updateuser, name="updateuser"),
    url(r'^users/(?P<id>\d+)/edit$', views.edituser, name="edituser"),
    url(r'^users/(?P<id>\d+)/delete$', views.deleteuser, name="deleteuser"),

]
