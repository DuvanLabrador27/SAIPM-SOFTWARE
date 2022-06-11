from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.forms import EmailField


#-------------------------CLASE USURIO-------------------------------------------

#Clase UseManager que me permiten crear un usuario y un superusuario, 
# teniendo en cuenta que la contraseña no se debe pasar como un texto plano se encripta en el modelo
class UserManager(BaseUserManager):

    def _create_user(self,username,email,password,is_staff, is_superuser,**extra_fields):
        usuario=self.model(
            username=username, 
            email=email, 
            is_staff=is_staff,
             is_superuser=is_superuser, 
             **extra_fields
       )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)       

    def create_superuser(self, username,email,password=None, **extra_fields):
        return self._create_user(username, email,password, True, True, **extra_fields)


#Usamos las clases AbstractBaseUser y permissionsMixin las cuales ya estan implementadas en Django
#AbstractBaseUser la usamos para personalizar nuestro usuario
#PermissionsMixin la usamos para darnos permisos a nuestro usuario
class Usuarios(AbstractBaseUser,PermissionsMixin):
    #id = models.AutoField(primary_key=True)
    #El id django lo crea de manera automatica, por ende no es necesario crearlo
    #El campo password no es necesario declararlo en el modelo, porque Django lo crea automaticamente
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    name= models.CharField(max_length=50, blank=True)
    level = models.IntegerField(null=True) 
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

   

#Configurar de que se va a usar un username para el acceso
    USERNAME_FIELD = 'username'

    #Hago el llamado de UserManager() para realizar mis acciones de usuario
    objects= UserManager()  

#Campo requerido para el registro de usuarios por consola
    REQUIRED_FIELDS = ['email',]


#Defino mi class meta para personalizar mi bd
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'



    #Metodo to string
    def __str__(self):
        return self.username 
