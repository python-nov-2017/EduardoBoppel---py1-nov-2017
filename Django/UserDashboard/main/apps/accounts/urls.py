from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [
    url(r'^register/$', views.UserRegistration.as_view(), name="register"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', login_required(auth_views.logout), name='logout'),
    
    url(r'^dashboard/$', login_required(views.ListUsers.as_view()), name="user_list"),
    url(r'^user/add/$', login_required(views.UserCreate.as_view()), name="user_add"),
    url(r'^user/(?P<pk>\d)/$', login_required(views.UserDetail.as_view()), name="user_detail"),
    url(r'^user/(?P<pk>\d)/edit/$', login_required(views.UserUpdate.as_view()), name="user_edit"),
    url(r'^user/(?P<pk>\d)/delete/$', login_required(views.UserDelete.as_view()), name="user_delete"),


]
