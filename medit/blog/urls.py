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
	url(r'^block-edit/$', views.block_edit, name='block_edit'),
	url(r'^block-edit.html/$', views.block_edit, name='block_edit'),
	url(r'^block-del/$', views.block_del, name='block_del'),
	
	url(r'^article-add/$', views.article_add, name='article_add'),
	url(r'^article-add.html/$', views.article_add, name='article_add'),
	url(r'^article-list.html/$', views.article_list, name='article_list'),
	url(r'^article-edit/$', views.article_edit, name='article_edit'),
	url(r'^article-edit.html/$', views.article_edit, name='article_edit'),
	url(r'^article-del/$', views.article_del, name='article_del'),
	
	url(r'^ck-upload-img/$', views.ck_upload_img, name='ck_upload_img'),
	
]
