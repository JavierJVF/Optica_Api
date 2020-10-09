from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from API import views
from API.views import *

router = DefaultRouter()
router.register(r'users', viewset=UserViewSet)
router.register(r'users/password', viewset=PasswordViewSet)
router.register(r'users/datos', viewset=UserAccountViewSet)
router.register(r'products', viewset=ProductViewSet)
router.register(r'ventas', viewset=VentasViewSet)
router.register(r'login', viewset=LoginViewSet)

urlpatterns = [
    url (r'', include(router.urls)),
]