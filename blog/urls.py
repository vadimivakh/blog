from django.conf.urls import url, include
# from blog.views import basic_one
from . import views

urlpatterns = [
    url(r'^1/', views.basic_one),
    url(r'^2/', views.basic_two),
    url(r'^posts/all', views.all_posts),
    url(r'^post/get/(?P<post_id>[0-9]+)/$', views.post_by_id),

]
