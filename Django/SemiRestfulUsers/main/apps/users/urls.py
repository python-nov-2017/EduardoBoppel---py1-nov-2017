from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="users"),   #GET / TEMPLATE
    url(r'^new/$', views.new, name="new"),   #GET / TEMPLATE WITH FORM
    url(r'^create/$', views.create, name="create"),   #POST, REDIRECT TO SHOW/ID
    url(r'^(?P<id>\d+)$', views.show, name="show"),   #GET / TEMPLATE
    url(r'^(?P<id>\d+)/edit$', views.edit, name="edit"),  #GET / TEMPLATE WITH FORM
    url(r'^(?P<id>\d+)/update$', views.update, name="update"),  #POST / REDIRECT TO USERS
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name="destroy"),  #GET, REDIRECT TO USERS
    

]
