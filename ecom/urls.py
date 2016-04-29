from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# Add product
	url(r'^add/$', 'ecom.views.add'),

	# view your waste
	url(r'^view/$', 'ecom.views.view'),

	# Delete waste
	url(r'^delete/(?P<prod_id>\d+)/$', 'ecom.views.delete')

)