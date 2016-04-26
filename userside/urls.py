from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# Userside index
	url(r'^$', 'userside.views.index'),

)
