

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from rest_framework.authtoken import views
from API.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^API/', include(('API.urls','API'), namespace='API')),
]

urlpatterns += [
    url(r'^API', include('rest_framework.urls', namespace='rest_framework')),
]
