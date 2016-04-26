from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# Create your views here.

@login_required(login_url='/',redirect_field_name=None)
def index(request):
	return render_to_response('userindex.html')