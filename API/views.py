from rest_framework import viewsets, status
from .models import Product, UserAccount, Ventas
from .serializers import ProductSerializer, UserAccountSerializer, VentasSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse 
from rest_framework.response import Response
from django.http import Http404
#import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
	queryset = UserAccount.objects.all()
	serializer_class = UserAccountSerializer


class VentasViewSet(viewsets.ModelViewSet):
	queryset = Ventas.objects.all()
	serializer_class = VentasSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		data = request.data.copy()
		#request.data._mutable = True
		data['password'] = make_password(data['password'])

		# set mutable flag back
		#request.data._mutable = _mutable

		serializer = self.get_serializer(data=data)

		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		password = request.POST.get('password')
		username = request.POST.get('username')
		
		user = User.objects.get(username=username)
		data = {'id':user.id, 'username':user.username, 'password':user.password,'email':user.email,'first_name':user.first_name,'last_name':user.last_name,'is_staff':user.is_staff}
		if user.check_password(password):
			#serializer = self.get_serializer(data=data)
			#serializer.is_valid(raise_exception=True)
			#headers = self.get_success_headers(serializer.data)
			return Response(data, status=status.HTTP_201_CREATED)
		else:
			return Response({'detail':'username o password incorrectos'}, status=status.HTTP_404_NOT_FOUND)

class PasswordViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def update(self, request, *args, **kwargs):
		dataU = request.data.copy()

		passwordOld = dataU['passwordOld']
		passwordNew = dataU['passwordNew']
		instance = self.get_object()
		user = self.get_object()
		
		if user.check_password(passwordOld):
			user.password = make_password(passwordNew)
			data = {'id':user.id, 'username':user.username, 'password':user.password,'email':user.email,'first_name':user.first_name,'last_name':user.last_name,'is_staff':user.is_staff}
			serializer = self.get_serializer(instance,data=data)
			serializer.is_valid(raise_exception=True)
			self.perform_update(serializer)
			headers = self.get_success_headers(serializer.data)
			return Response(serializer.data, status=200)
		else:
			return Response({'detail':'password incorrecto'}, status=status.HTTP_404_NOT_FOUND)			