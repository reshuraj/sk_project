
from django.conf.urls import url
from django.contrib import admin
from sk.views import *

urlpatterns = [
    url(r'^$', index),
    
    url(r'^gallery/$', gallery),
]
