from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hello-world/', include('hello_world.urls')),
    path('admin/', admin.site.urls),
]
