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
    
    #Validar que las contraseñas sean iguales
    def clean_password2(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            self.add_error('password2', 'Las contraseñas no coinciden')
        