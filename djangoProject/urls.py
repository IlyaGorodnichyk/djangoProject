from django.contrib import admin
from django.urls import path, include


#Настройка панели администратора
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts', include("django.contrib.auth.urls")),
]
