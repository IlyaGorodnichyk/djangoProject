from django.contrib import admin
from main.models import Order
#Настройка отображения заявки в панели администратора
admin.site.register(Order)


