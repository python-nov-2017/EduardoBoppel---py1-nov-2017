from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d)/$', login_required(views.MessageList.as_view()), name="message_list"),
    url(r'^(?P<pk>\d)/(?P<id>\d)/$', login_required(views.PostComment.as_view()), name="post_comment"),
    
]
