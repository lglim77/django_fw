"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/post/new/$', views.post_new2, name='post_new'),
    url(r'^blog/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^blog/post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^blog/post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
		url(r'^blog/comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
		url(r'^blog/comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]
