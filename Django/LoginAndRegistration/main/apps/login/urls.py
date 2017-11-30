from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/$', views.home),
    url(r'^logout/$', views.logout),

    #### METHOD 1: HTML FORM AND MODEL MANAGER
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),

    #### METHOD 2: NORMAL FORM
    url(r'^registernormalform/$', views.registernormalform),
    url(r'^loginnormalform/$', views.loginnormalform),
    
    #### METHOD 3: MODEL FORM
    url(r'^registermodelform/$', views.registermodelform),
]
