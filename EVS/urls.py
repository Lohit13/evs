from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'audnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^logout/', 'audnet.views.logout'),

    url(r'^$', 'EVS.views.index', name='home'), #index page

    # Userside urls
    (r'^user/', include('userside.urls')),	


)
