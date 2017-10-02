from django.conf.urls import url, include
from . import views
from blog_django import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from .models import Post
from .views import PostListView, PostDetailView, TagPostList
from .forms import EditPostForm

urlpatterns = [
    url(r'^$', PostListView.as_view(), name="index"),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.PostDetailView.as_view(), name="post_by_id"),
    url(r'^posts/addcomment/(?P<post_id>[0-9]+)/$', views.CreateCommentView.as_view(), name="add_comment"),
    url(r'^posts/addpost/$', views.CreatePostView.as_view(), name="add_post"),
    url(r'^posts/editpost/(?P<post_id>[0-9]+)/$', views.UpdatePostView.as_view(), name="editpost"),
    url(r'^posts/deletepost/(?P<post_id>[0-9]+)/$', views.delete_post, name="deletepost"),
    url(r'^posts/post_by_tag/tag=(?P<tag_name>\w+)/$', views.TagPostList.as_view(), name="post_by_tag"),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
