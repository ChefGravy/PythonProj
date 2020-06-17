from django.shortcuts import render
#this will need to be connected to a form later on

from django.urls import reverse_lazy
from django.views.generic import CreateView

#forms for logging in
from . import forms

# cReate your views here.

class SignUp(CreateView):
    #pass for now since we want to add more.
    #use 'pass' to avoid
    #not instantiate with () class
    #this is now connected to forms.py via form_class
    form_class = forms.UserCreateForm
    #once someone signed up, upon success, it will send back to login with reverse lazy
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
