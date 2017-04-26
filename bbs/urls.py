from django.conf.urls import include, url
from . import views

app_name = 'bbs'
urlpatterns = [
    # ex: /bbs/
    url(r'^$', views.post_list, name='post_list'),
    # ex: /bbs/5
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    # ex: /bbs/5/edit
    url(r'^(?P<post_id>\d+)/edit/$', views.edit_post, name='post_edit'),
    # ex: /bbs/add
    url(r'add/$', views.edit_post, name='post_edit'),
    # ex: /bbs/5/delete
    url(r'^(?P<post_id>\d+)/delete/$', views.delete_post, name='post_delete')
    # ex: /bbs/5/add_comment
    url(r'^(?P<post_id>\d+)/add_comment/$', views.edit_comment, name='comment_edit')
    # ex: /bbs/5/1/edit
    url(r'^(?P<post_id>\d+)/(?P<comment_id>\d+)/edit/$', views.edit_comment, name='comment_edit')
]
