from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from userside.models import *
from userside.views import retUser
from ngo.models import *
from ecom.models import *


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

@login_required(login_url='/',redirect_field_name=None)
def bengo(request):
	email = retUser(request.user.email)
	print 'enterenterenter'

	args = {}

	if request.method == 'POST':
		print 'yayayayay'
		name = request.POST['name']
		address = request.POST['address']
		phno = request.POST['phno']
		obj = request.POST['obj']
		chair = request.POST['chair']

		if len(name)<1 or len(address)<1 or len(phno)<1 or len(obj)<1 or len(chair)<1:
			args['error'] = "Please fill all fields"
			return render_to_response('bengo.html',args)

		###### ENTER INTO DB
		ngo = NGO(email=email,name=name,address=address,phno=phno,obj=obj,chair=chair)
		ngo.save()
		print 'ayayayayay'

		args['error'] = "Your request has been logged. We will contact you shortly"

	args.update(csrf(request))

	return render_to_response('bengo.html',args)


@login_required(login_url='/',redirect_field_name=None)
def beecom(request):
	email = retUser(request.user.email)

	args = {}

	if request.method == 'POST':
		name = request.POST['name']
		address = request.POST['address']
		phno = request.POST['phno']
		cname = request.POST['cname']

		if len(name)<1 or len(address)<1 or len(phno)<1 or len(cname)<1:
			args['error'] = "Please fill all fields"
			return render_to_response('beecom.html',args)

		###### ENTER INTO DB
		ecom = ECOM(email=email,name=name,address=address,phno=phno,cname=cname)
		ecom.save()

		args['error'] = "Your request has been logged. We will contact you shortly"

	args.update(csrf(request))

	return render_to_response('beecom.html',args)


