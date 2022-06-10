from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from django.forms import forms

from .forms import UserRegisterForm

# Create your views here.
class UserRegister(CreateView):
    template_name = 'usuarios/user_register.html'
    form_class= UserRegisterForm
    success_url = '/'
