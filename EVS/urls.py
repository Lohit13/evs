from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EVS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^logout/', 'EVS.views.logout'),

    url(r'^$', 'EVS.views.index', name='home'), #index page
    url(r'^ngo/register$', 'EVS.views.bengo', name='bengo'), #register ngo
    url(r'^ecom/register$', 'EVS.views.beecom', name='beecom'), #register ecom  

    # Userside urls
    (r'^user/', include('userside.urls')),	

    # ECOM urls
    (r'^ecom/', include('ecom.urls')),


)
