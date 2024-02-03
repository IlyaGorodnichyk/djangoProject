from django.shortcuts import render
from main.models import Order

def index(request):
    return render(request, 'main/index.html')

#Сохранения информации в базе данных и отображение страницы с благодарностью
def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(appointment_name=name, appointment_phone=phone)
    element.save()
    return render(request, 'main/thanks_page.html', {'name': name,
                                                     'phone': phone})
