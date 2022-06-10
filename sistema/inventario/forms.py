from django import forms
from .models import Usuarios

class UserRegisterForm(forms.ModelForm):

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

    class Meta:
        model = Usuarios
        fields = ['username', 'email','nombres','apellidos','nivel',]