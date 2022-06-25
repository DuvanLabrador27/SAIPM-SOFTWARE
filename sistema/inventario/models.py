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
    
#-------------------------------PRODUCTO------------------------------------------------
class Producto(models.Model):
    #id
    decisiones =  [('1','Masa lista'),('2','PasaPalos')]
    decisionesTamanio =  [('1','Grande empanada 560g'),('2','Mediana empanada 500g'),('3','Pequeña empanda 450g'),('4','Grande flauta 600g'),('5','Pequeña flauta 550g'),('6','PasaPalos 450g')]
    nombreProducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500, blank=True)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    disponible = models.IntegerField(null=True)
    tamanio = models.CharField(max_length=20,choices=decisionesTamanio)
    categoria = models.CharField(max_length=20,choices=decisiones)

    def __str__(self):
        return self.nombreProducto

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    
#---------------------------------------------------------------------------------------



#-------------------------------CLIENTE------------------------------------------------
class Cliente(models.Model):
    #id
    identificacion = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    direccion  = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    decisionesId =  [('1','CC'),('2','Pasa Porte')]
    categoriaId = models.CharField(max_length=20,choices=decisionesId)
    idUsuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

#-------------------------------COTIZACION------------------------------------------------
class Cotizacion(models.Model):
    #id
    descripcion = models.CharField(max_length=40)
    fecha= models.DateTimeField(auto_now_add=True)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'cotizacion'
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizacion'

#-------------------------------FACTURA------------------------------------------------
class Factura(models.Model):
    #id
    fecha= models.DateTimeField(auto_now_add=True)
    cotizacionId = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)


    class Meta:
        db_table = 'factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
    
#-------------------------------DETALLE FACTURA------------------------------------------------
class DetalleFactura(models.Model):
    #id
    total= models.DecimalField(max_digits=9,decimal_places=2)
    facturaId = models.ForeignKey(Factura, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        db_table = 'facturaDetalle'
        verbose_name = 'FacturaDetalle'
        verbose_name_plural = 'FacturasDetalles'









