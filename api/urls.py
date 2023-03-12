from django.contrib import admin
from django.urls import path, include
from backend.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routerBackend.urls))
]
