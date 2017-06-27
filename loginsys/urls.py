from django.conf.urls import url, include
# from blog.views import basic_one
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),

]
