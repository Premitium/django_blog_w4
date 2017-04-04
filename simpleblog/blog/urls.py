from django.conf.urls import url

from .views import index, create_blog_post, login_view, profile_view, single_post_show


urlpatterns = [
    url(r'^$|index', index, name='index'),
    url(r'^login/$', login_view, name='login'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^create/$', create_blog_post, name='create'),
    url(r'^single-post/(?P<title>.*)', single_post_show, name='single-post')
]

"""Must do: read more about regex"""
