from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'google', views.google, name='google'),
	url(r'^$', views.post_list, name='post_list'),
]