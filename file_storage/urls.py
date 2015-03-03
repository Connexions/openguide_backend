from django.conf.urls import patterns, url
from file_storage import views

urlpatterns = patterns('',
  url(r'^images/upload', views.upload, name='upload'),
)
