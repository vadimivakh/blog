from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^members/', include('user_profile.urls')),
]
