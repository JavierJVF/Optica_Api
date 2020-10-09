from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from API import views
from API.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = DefaultRouter()
router.register(r'users', viewset=UserViewSet)
router.register(r'users/datos', viewset=UserAccountViewSet)
router.register(r'products', viewset=ProductViewSet)
router.register(r'ventas', viewset=VentasViewSet)
router.register(r'login', viewset=LoginViewSet)
router.register(r'books', viewset=BookViewSet)

urlpatterns = [
    url (r'', include(router.urls))
]