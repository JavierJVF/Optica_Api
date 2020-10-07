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
		_mutable = request.data._mutable
		request.data._mutable = True
		request.data['password'] = make_password(request.data['password'])

		# set mutable flag back
		request.data._mutable = _mutable
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		#serializer.data['password'] = make_password(serializer.data['password'])
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED)