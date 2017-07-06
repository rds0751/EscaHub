from django.conf.urls import url
from EscaHub.blog import views

urlpatterns = [
	url(r'^$', views.blogs, name='blogs'),
    url(r'^write/$', views.write, name='write'),
    url(r'^preview/$', views.preview, name='preview'),
    url(r'^drafts/$', views.drafts, name='drafts'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^tag/(?P<tag_name>.+)/$', views.tag, name='tag'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit_blog'),
    url(r'^(?P<slug>[-\w]+)/$', views.blog, name='blog'),
]