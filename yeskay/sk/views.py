from django.shortcuts import render
from django.shortcuts import render_to_response
import MySQLdb
from MySQLdb import cursors
from django.contrib.auth import authenticate
from sk.models import *
from django.http import HttpResponseRedirect
from sk.forms import *
from django.template import RequestContext
#from django.contrib import messages
#from django.contrib.auth import authenticate, login

# Create your views here.

def contact(request):
	return render(request,'/home/ubuntu/yeskay/sk/templates/sk/contact.html',{})

def submit(request):
	#return render_to_response('/sk/templates/project.html',{})
	print "hii"
	if request.method == 'POST':
		print "okay"
        	form1 = ContactForm(request.POST)
		print form1.errors.as_data()
        	if form1.is_valid():
			print "name"
			#print form1.is_valid()
			#name=name.save()
			#name=form.data['name']
			#email=form.data['email']
			#phone=form.data['phone']
			#message=form.data['message']
        		name=form1.cleaned_data['name']
			email=form1.cleaned_data['email']
			phone=form1.cleaned_data['phone']
			message=form1.cleaned_data['message']
          
           		a=Contact( 
                		name= name,
				email= email,
				phone= phone ,
				message= message 
                 		 )
           		a.save()
			print "name",name
	 	return render(request,'/home/ubuntu/yeskay/sk/templates/sk/contact.html')
	else:
       		return render(request,'/home/ubuntu/yeskay/sk/templates/sk/contact.html')
       
