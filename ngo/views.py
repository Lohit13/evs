from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from userside.models import*

def retUser(email):
	try:
		user = UserProfile.objects.get(email=email)
	except:
		user = UserProfile()
		user.email = email
		user.save()
	return user


@login_required(login_url='/',redirect_field_name=None)
def view(request):
	email = retUser(request.user.email)

	if not email.isNgo:
		return HttpResponseRedirect('/user/')

	args = {}
	args.update(csrf(request))

	a = Ewaste.objects.all()

	args['objs'] = a
	args['userprofile'] = user

	return render_to_response('viewall.html',args)

@login_required(login_url='/',redirect_field_name=None)
def collect(request,waste_id=1):
	email = retUser(request.user.email)

	if not email.isNgo:
		return HttpResponseRedirect('/user/')

	if request.method=='POST':
		print 'sfsedf'
		points = request.POST['points']

		if not points.isdigit():
			return HttpResponseRedirect('/ngo/view/')

		print 'two'

		points = int(points)

		w = Ewaste.objects.get(id=waste_id)

		o = Offer(waste = w, ngo = email)

		o.save()
		print 'one'

	return HttpResponseRedirect('/ngo/view')

