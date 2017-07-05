from django.conf.urls import url, include
from . import views
from blog_django import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.all_posts),
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_by_id),
    # url(r'^posts/addlike/(?P<post_id>[0-9]+)/$', views.add_like),
    url(r'^posts/addcomment/(?P<post_id>[0-9]+)/$', views.add_comment),
    url(r'^posts/addpost/$', views.add_post),
    url(r'^login/$', views.login),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
