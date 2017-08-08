from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.user_profile),
    url(r'^edit_profile/(?P<user_id>[0-9]+)/$', views.edit_user_profile),

]
