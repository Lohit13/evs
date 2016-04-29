from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# Userside index
	url(r'^$', 'userside.views.index'),

	# Add ewaste
	url(r'^add/$', 'userside.views.add'),

	# view your waste
	url(r'^view/$', 'userside.views.view'),

	# Delete waste
	url(r'^delete/(?P<waste_id>\d+)/$', 'userside.views.delete')

)
