from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# Create your views here.

# Creates new user/Returns existing user
def retUser(email):
	try:
		user = UserProfile.objects.get(email=email)
	except:
		user = UserProfile()
		user.email = email
		user.save()
	return user


@login_required(login_url='/',redirect_field_name=None)
def index(request):
	user = retUser(request.user.email)

	return render_to_response('userindex.html')