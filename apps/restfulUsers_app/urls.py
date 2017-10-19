from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.newPage),
	url(r'^(?P<id>\d+)/edit$', views.editPage),
	url(r'^(?P<id>\d+)/update$', views.updateUser),
	url(r'^(?P<id>\d+)$', views.userPage),
	url(r'^create$', views.createUser),
	url(r'^(?P<id>\d+)/destroy$', views.destroy),
]