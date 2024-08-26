
from django.contrib import admin
from django.urls import path,include
from myapp.views import display


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('disp/',display),
    path('gt/',include('myapp.urls')),




    gana
    
]
