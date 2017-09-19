from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^members/', include('user_profile.urls')),
    # url(r'^login/', include('loginsys.urls')),
]
