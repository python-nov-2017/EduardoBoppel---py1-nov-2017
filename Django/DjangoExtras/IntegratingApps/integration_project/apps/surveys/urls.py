from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process_survey$', views.process_survey, name="process"),
    url(r'^results$', views.results, name="results")
]