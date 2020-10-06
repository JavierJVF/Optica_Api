from rest_framework import viewsets, status
from .models import Product, UserAccount, Ventas
from .serializers import ProductSerializer, UserAccountSerializer, VentasSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse 
from rest_framework.response import Response
from django.http import Http404
import requests
from django.contrib.auth.models import User

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