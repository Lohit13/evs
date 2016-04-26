from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf

#Logs the user out
def logout(request):
	auth_logout(request)
	args = {}
	args.update(csrf(request))
	return index(request)

def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/user/')
	return render_to_response('index.html')