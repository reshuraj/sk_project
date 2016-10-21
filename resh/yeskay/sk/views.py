from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.shortcuts import render
from sk.models import Contact
from django.http import HttpResponseRedirect
# Create your views here.

def contact(request):
	return render(request,'/home/ubuntu/yeskay/sk/templates/sk/contact1.html',{})

def submit(request):
	#return render_to_response('/sk/templates/project.html',{})
	
	if request.method == 'POST':
		print "okay"
        	form1 = ContactForm(request.POST)
        	if form1.is_valid():
			#name=name.save()
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
	 	return redirect('/home/ubuntu/yeskay/sk/templates/sk/contact1.html')
	else:
       		return render_to_response('/home/ubuntu/yeskay/sk/templates/sk/contact1.html',{})
       
