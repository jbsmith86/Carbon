from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carbonpaper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name='home'),
    url(r'^(?P<slug>[\w\-]+)/$','blog.views.post'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
