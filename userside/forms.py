from django import forms 
from models import *


class EwasteForm(forms.ModelForm):
	
	class Meta:
		model = Ewaste
		fields = ('name','desc','bought_on','pic')
