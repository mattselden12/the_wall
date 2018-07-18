from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^wall/$', views.wall),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^logoff/$', views.logoff),
    url(r'^postmessage/$', views.postmessage),
    url(r'^postcomment/$', views.postcomment),
    url(r'^deletemessage/$', views.deletemessage),
]