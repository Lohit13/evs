from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from userside.models import *
from userside.forms import EwasteForm
from ecom.models import *

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

	args={}

	a = Offer.objects.filter(waste__user=user)

	args['offers'] = a
	args['userprofile'] = user

	return render_to_response('userindex.html',args)


@login_required(login_url='/',redirect_field_name=None)
def add(request):
	email = retUser(request.user.email)

	args = {}

	if request.method == 'POST':
		print 'yayay'
		form = EwasteForm(request.POST, request.FILES)
		print 'sfsdf'
		print form
		if form.is_valid():
			print 'wdawdadwa'
			f2 = form.save(commit=False)
			f2.user = email
			f2.save()
			print 'sdfzdvds'

		args['error'] = "Your request has been logged. We will contact you shortly"

	form = EwasteForm()
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('add.html',args)

@login_required(login_url='/',redirect_field_name=None)
def view(request):
	email = retUser(request.user.email)

	args = {}

	a = Ewaste.objects.filter(user=email)

	args['ewaste'] = a

	return render_to_response('view.html',args)

@login_required(login_url='/',redirect_field_name=None)
def delete(request,waste_id=1):
	email = retUser(request.user.email)

	args = {}

	a = Ewaste.objects.get(id=waste_id)

	if a.user == email:
		a.delete()

	return HttpResponseRedirect('/user/view/')

@login_required(login_url='/',redirect_field_name=None)
def viewoffers(request):
	email = retUser(request.user.email)

	args = {}

	a = Offer.objects.filter(waste__user=email)

	args['offers'] = a

	return render_to_response('viewoffers.html',args)


@login_required(login_url='/',redirect_field_name=None)
def accept(request,offer_id=1):
	user = retUser(request.user.email)

	args = {}

	offer = Offer.objects.get(id=offer_id)

	if not offer.waste.user == user:
		return HttpResponseRedirect('/user/viewoffers/')

	waste = offer.waste
	user.points += offer.points
	user.save()
	waste.delete()
	offer.delete()

	return HttpResponseRedirect('/user/viewoffers/')


@login_required(login_url='/',redirect_field_name=None)
def viewproducts(request):
	email = retUser(request.user.email)

	args = {}

	a = Product.objects.all()

	args['products'] = a

	return render_to_response('viewproducts.html',args)