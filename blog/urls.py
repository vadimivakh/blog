from django.conf.urls import url, include
from . import views
from blog_django import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.all_posts, name="index"),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_by_id, name="post_by_id"),
    url(r'^posts/addcomment/(?P<post_id>[0-9]+)/$', views.add_comment, name="add_comment"),
    url(r'^posts/addpost/$', views.add_post, name="add_post"),
    url(r'^posts/editpost/(?P<post_id>[0-9]+)/$', views.edit_post, name="editpost"),
    url(r'^posts/deletepost/(?P<post_id>[0-9]+)/$', views.delete_post, name="deletepost"),
    url(r'^posts/post_by_tag/tag=(?P<tag_name>\w+)/$', views.post_by_tag, name="post_by_tag"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
