import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.forms import ModelForm 
from sk.models import Contact 
#class ContactForm(ModelForm):class Meta:


class ContactForm(forms.Form):

	name=forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=30)),  label=_("name"))
	email=forms.EmailField(widget=forms.TextInput(attrs=dict(required=False, max_length=30)),  label=_("email"))
	phone=forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=30)),  label=_("phone"))
	message=forms.CharField(widget=forms.TextInput(attrs=dict(required=False, max_length=30)),  label=_("message"))

	
 

	

	

			
