from django.conf.urls import url

from .views import index, create_blog_post, login_view, profile_view, single_post


urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^create/$', create_blog_post, name='create'),
    url(r'^single-post/(?P<id>[0-9]+)/$', single_post, name='single-post'),
    url(r'^$', index, name='index')
]

"""Must do: read more about regex"""
