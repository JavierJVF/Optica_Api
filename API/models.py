from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_path(instance, filname):
    return '/'.join([filname])

class Book(models.Model):
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)

class Product(models.Model):
	modelosValidos = (
       ('convencional', 'convencional'),
       ('cosmeticos', 'cosmeticos'),
       ('de contacto', 'de contacto'),
   )
   
	nombre = models.CharField(max_length = 255, unique=True)
	modelo = models.CharField(max_length = 30, choices=modelosValidos, default='convencional')
	marca = models.CharField(max_length = 255)
	descripcion = models.TextField()
	precio = models.IntegerField()
	stock = models.IntegerField()
	cover = models.ImageField(blank=True, null=True, upload_to=upload_path)

class UserAccount(models.Model):
	user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
	#nombre = models.CharField(max_length = 255)
	#apellido = models.CharField(max_length = 255)
	direccion = models.CharField(max_length = 255)
	telefono = models.CharField(max_length = 255)

class Ventas(models.Model):
	fechaCompra = models.DateField(auto_now_add=True)
	CantidadDeUnidades = models.IntegerField()
	precioTotal = models.FloatField(default=0)
	idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
	idUserrAccount = models.ForeignKey(User, on_delete=models.CASCADE)