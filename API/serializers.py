from .models import Product, UserAccount, Ventas
from rest_framework import serializers
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ['id', 'nombre', 'modelo', 'marca', 'descripcion', 'precio', 'stock',]

class UserAccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserAccount
		#fields = ['id', 'user', 'nombre', 'apellido', 'direccion', 'telefono',]
		fields = ['id', 'user', 'direccion', 'telefono',]

class VentasSerializer(serializers.ModelSerializer):

	class Meta:
		model = Ventas
		fields = ['id', 'fechaCompra', 'CantidadDeUnidades', 'idProduct', 'idUserrAccount',]

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name','is_staff']
		write_only_fields = ('password',)
		read_only_fields = ('id',)
