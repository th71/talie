from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^',include('load.urls')),
    url(r'^interface1/', include('interface1.urls')),
    url(r'^admin/', admin.site.urls),
]
