from django import forms 
from models import *


class EwasteForm(forms.ModelForm):
	
	class Meta:
		model = Ewaste

		def __init__(self, *args, **kwargs):
			super(MyForm, self).__init__(*args, **kwargs)
			self.fields['name'].widget.attrs.update({'class' : 'form-control'})
			self.fields['desc'].widget.attrs.update({'class' : 'form-control'})
			self.fields['bought_on'].widget.attrs.update({'class' : 'form-control'})
			self.fields['pic'].widget.attrs.update({'class' : 'form-control'})


			self.fields['name'].widget.attrs.update({'placeholder' : 'name'})
			self.fields['desc'].widget.attrs.update({'placeholder' : 'desc'})
			self.fields['bought_on'].widget.attrs.update({'placeholder' : 'bought_on'})
			self.fields['pic'].widget.attrs.update({'placeholder' : 'pic'})


		fields = ('name','desc','bought_on','pic')
