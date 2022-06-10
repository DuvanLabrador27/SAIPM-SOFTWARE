from django import forms
from .models import Usuarios

#Formulario para registrar usuarios
class UserRegisterForm(forms.ModelForm):

#-----------Validar Contraseña-------------
    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
           }
        )

    )
    password2=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Repetir Contraseña'
           }
        )

    )

#Definiendo los archivos que se van a ver en mi formulario
    class Meta:
        model = Usuarios
        fields = ['username', 'email', 'nombres', 'apellidos', 'nivel', 'is_staff',]