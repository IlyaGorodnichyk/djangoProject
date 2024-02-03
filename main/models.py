from django.db import models

# Валидация полей вода информации
class Order(models.Model):
 appointment_dt = models.DateTimeField(auto_now=True)
 appointment_name = models.CharField('Имя', max_length=200)
 appointment_phone = models.CharField('Номер', max_length=200)

 def __str__(self):
     return self.appointment_name
#Отображения "Заявка в базе данных"
 class Meta:
     verbose_name = 'Заявка'
     verbose_name_plural = 'Заявки'