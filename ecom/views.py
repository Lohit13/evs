from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from ecom.models import *
from ecom.forms import ProductForm
from userside.models import *

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
def add(request):
	email = retUser(request.user.email)

	if not email.isEcom:
		return HttpResponseRedirect('/user/')

	args = {}

	if request.method == 'POST':
		print 'yayay'
		form = ProductForm(request.POST, request.FILES)
		print 'sfsdf'
		print form
		if form.is_valid():
			print 'wdawdadwa'
			f2 = form.save(commit=False)
			f2.user = email
			f2.save()
			print 'sdfzdvds'

		args['error'] = "Your request has been logged. We will contact you shortly"

	form = ProductForm()
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('addproduct.html',args)

@login_required(login_url='/',redirect_field_name=None)
def view(request):
	email = retUser(request.user.email)

	if not email.isEcom:
		return HttpResponseRedirect('/user/')

	args = {}

	a = Product.objects.filter(user=email)

	args['prod'] = a

	return render_to_response('viewprod.html',args)

@login_required(login_url='/',redirect_field_name=None)
def delete(request,prod_id=1):
	email = retUser(request.user.email)

	if not email.isEcom:
		return HttpResponseRedirect('/user/')

	args = {}

	a = Product.objects.get(id=prod_id)

	if a.user == email:
		a.delete()

	return HttpResponseRedirect('/ecom/view/')

@login_required(login_url='/',redirect_field_name=None)
def buy(request,prod_id=1):
	user = retUser(request.user.email)

	p = Product.objects.get(id=prod_id)

	if p.points > user.points:
		return HttpResponseRedirect('/user/')

	user.points -= p.points
	user.save()

	p.delete()

	return HttpResponseRedirect('/user/viewproducts/')