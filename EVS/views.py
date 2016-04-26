from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout

#Logs the user out
def logout(request):
	auth_logout(request)
	args = {}
	args.update(csrf(request))
	return index(request)

def index(request):
	return render_to_response('index.html')