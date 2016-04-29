from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# Add product
	url(r'^add/$', 'ecom.views.add'),

	# view your products
	url(r'^view/$', 'ecom.views.view'),

	# Delete product
	url(r'^delete/(?P<prod_id>\d+)/$', 'ecom.views.delete'),

	# Buy product
	url(r'^buy/(?P<prod_id>\d+)/$', 'ecom.views.buy'),

)