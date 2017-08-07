from django.conf.urls import url, include
# from blog.views import basic_one
from . import views
from blog_django import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),

]
