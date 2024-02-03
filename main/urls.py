
from django.urls import path
from . import views

#Переход по HTML страницам
urlpatterns = [
    path('', views.index),
    path('thanks', views.thanks_page,  name ='thanks_page'),
]
