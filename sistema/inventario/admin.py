from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import LoginFormulario
from .models import Usuarios

class UsuarioAdmin(UserAdmin):
    add_form = LoginFormulario
    #form = CustomUserChangeForm
    model = Usuarios
    list_display = ['email', 'username',]

admin.site.register(Usuarios, UsuarioAdmin)