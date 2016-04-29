from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# Userside index
	url(r'^$', 'userside.views.index'),

	# Add ewaste
	url(r'^add/$', 'userside.views.add'),

	# view your waste
	url(r'^view/$', 'userside.views.view'),

	# Delete waste
	url(r'^delete/(?P<waste_id>\d+)/$', 'userside.views.delete'),

	# view offers
	url(r'^viewoffers/$', 'userside.views.viewoffers'),

	# Accept offer
	url(r'^accept/(?P<offer_id>\d+)/$', 'userside.views.accept'),

	# view products
	url(r'^viewproducts/$', 'userside.views.viewproducts'),

)
