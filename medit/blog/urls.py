from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.test, name='test'),
    url(r'^test/$', views.test, name='test'),
	url(r'^login/$', views.login, name='login'),
	url(r'^index/$', views.index, name='index'),
	url(r'^block-add/$', views.block_add, name='block_add'),
	url(r'^block-add.html/$', views.block_add, name='block_add'),
	url(r'^block-list.html/$', views.block_list, name='block_list'),
]
