from django.conf.urls import url, include
# from blog.views import basic_one
from . import views

urlpatterns = [
    url(r'^$', views.all_posts),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_by_id),
    url(r'^posts/addlike/(?P<post_id>[0-9]+)/$', views.add_like),
    url(r'^posts/addcomment/(?P<post_id>[0-9]+)/$', views.add_comment),
]
