from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('testepratico/', include('testepratico.urls')),
    path('admin/', admin.site.urls),
]