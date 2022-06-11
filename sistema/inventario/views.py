from django.shortcuts import render
from django.views.generic import (
    CreateView
)

from django.views.generic.edit import (
    FormView
)

from django.forms import forms

from .forms import UserRegisterForm

from .models import Usuarios

# Create your views here.

#Creando vista para mi formulario registrar usuarios
class UserRegister(FormView):
    template_name = 'usuarios/user_register.html'
    form_class= UserRegisterForm
    success_url = '/'

#Recuperamos nuestros datos, me permite guardar mi contraseña encriptada
    def form_valid(self, form):
        Usuarios.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            nivel=form.cleaned_data['nivel'],
        )
        return super(UserRegister, self).form_valid(form)
