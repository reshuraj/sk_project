from __future__ import unicode_literals

from django.db import models
#from django.forms import ContactForm

# Create your models here.

class Contact(models.Model):

	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	message=models.CharField(max_length=200)
