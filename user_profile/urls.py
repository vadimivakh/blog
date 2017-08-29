from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.user_profile),
    url(r'^edit_profile/(?P<user_id>[0-9]+)/$', views.edit_user_profile),
    url(r'^user_posts/user_id=(?P<user_id>[0-9]+)/$', views.user_posts),
    url(r'^user_comments/user_id=(?P<user_id>[0-9]+)/$', views.user_comments),
    url(r'^delete_profile/user_id=(?P<user_id>[0-9]+)/$', views.delete_profile),

]
