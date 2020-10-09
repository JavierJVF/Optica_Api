

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from rest_framework.authtoken import views
from API.urls import urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^API/', include(('API.urls','API'), namespace='API')),
]

urlpatterns += [
    url(r'^API', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
