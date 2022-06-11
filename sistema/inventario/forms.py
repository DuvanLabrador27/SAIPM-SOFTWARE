from django import forms
from .models import Usuarios,Producto

from django.forms import ModelChoiceField




class LoginFormulario(forms.Form):
    username = forms.CharField(label="Tu nombre de usuario",widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario',
        'class': 'form-control underlined', 'type':'text','id':'user'}))

    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
        'class': 'form-control underlined', 'type':'password','id':'password'}))




class UsuarioFormulario(forms.Form):
    is_active =  [ ('1','Administrador'),('0','Usuario') ]

    username = forms.CharField(
        label = "Nombre de usuario",
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un nombre de usuario',
        'id':'username','class':'form-control','value':''} ),
        )

    name = forms.CharField(
        label = 'Nombre',
        max_length = 100,
        widget = forms.TextInput(attrs={'class':'form-control','id':'name','placeholder':'Inserte un nombre','value':''}), 
        )

    email = forms.CharField(
        label = 'Correo electronico',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un correo valido',
        'id':'email','class':'form-control','type':'email','value':''} )
        )

    is_active =  forms.CharField(
        required=False,
        label="Nivel de acceso",
        max_length=2,
        widget=forms.Select(choices=is_active,attrs={'placeholder': 'El nivel de acceso',
        'id':'level','class':'form-control','value':''}
        )
        )

class NuevoUsuarioFormulario(forms.Form):
    is_active =  [ ('1','Administrador'),('0','Usuario') ]

    username = forms.CharField(
        label = "Nombre de usuario",
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un nombre de usuario',
        'id':'username','class':'form-control','value':''} ),
        )

    name = forms.CharField(
        label = 'Nombre',
        max_length = 100,
        widget = forms.TextInput(attrs={'class':'form-control','id':'name','placeholder':'Inserte un nombre','value':''}), 
        )

    email = forms.CharField(
        label = 'Correo electronico',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un correo valido',
        'id':'email','class':'form-control','type':'email','value':''} )
        )    

    password = forms.CharField(
        label = 'Clave',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte una clave',
        'id':'password','class':'form-control','type':'password','value':''} )
        )  

    rep_password = forms.CharField(
        label = 'Repetir clave',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Repita la clave de arriba',
        'id':'rep_password','class':'form-control','type':'password','value':''} )
        )  

    is_active =  forms.CharField(
        label="Nivel de acceso",
        max_length=2,
        widget=forms.Select(choices=is_active,attrs={'placeholder': 'El nivel de acceso',
        'id':'level','class':'form-control','value':''}
        )
        )


class ClaveFormulario(forms.Form):
    

    clave_nueva = forms.CharField(
        label = 'Ingrese la clave nueva',
        max_length=50,
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte la clave nueva de acceso',
        'id':'clave_nueva','class':'form-control', 'type': 'password'}),
        )

    repetir_clave = forms.CharField(
        label="Repita la clave nueva",
        max_length=50,
        widget = forms.TextInput(
        attrs={'placeholder': 'Vuelva a insertar la clave nueva',
        'id':'repetir_clave','class':'form-control', 'type': 'password'}),
        )
#-----------------------------------------------------------------------------------------

class ProductoFormulario(forms.ModelForm):
    precio = forms.DecimalField(
        min_value = 0,
        label = 'Precio',
        widget = forms.NumberInput(
        attrs={'placeholder': 'Precio del producto',
        'id':'precio','class':'form-control'}),
        )
    class Meta:
        model = Producto
        fields = ['descripcion','precio','disponible','categoria']
        labels = {
        'descripcion': 'Nombre',
        
        }
        widgets = {
        'descripcion': forms.TextInput(attrs={'placeholder': 'Nombre del producto',
        'id':'descripcion','class':'form-control'} ),

        'disponible': forms.TextInput(attrs={'class':'form-control','placeholder': 'Disponibilidad del producto'}),
        
        'categoria': forms.Select(attrs={'class':'form-control','id':'categoria'})
        }

