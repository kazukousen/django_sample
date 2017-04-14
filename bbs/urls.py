from django.conf.urls import include, url
from . import views

app_name = 'bbs'
urlpatterns = [
    # ex: /bbs/
    url(r'^$', views.post_list, name='index')
]
