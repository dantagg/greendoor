from django.conf.urls import patterns, include, url

import bgdapp.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bgdapp.views.everything', name='home'),
#    url(r'^/stories$', 'bgdapp.views.stories', name='stories'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
