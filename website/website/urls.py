
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^comedy/', include('comedy.urls')),
    url(r'^sports/', include('sports.urls')),
    url(r'^videos/', include('videos.urls')),
]
