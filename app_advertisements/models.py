from django.db import models
from django.contrib import admin
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
# создаем таблицу и модель с помощью наследования
class Advertisement(models.Model):
    # создаем столбец заголовков в нашей таблице
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    # столбец - описание
    description = models.TextField(verbose_name="Описание")
    # столбец - цены макс 10 чисел и 2 после запятой
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField(verbose_name="Торг", help_text="Отметьте, если торг уместен")
    # столбцы дат с автоматическим заполнением
    created_at = models.DateTimeField(auto_now_add=True) # автоматом при добавлении
    updated_at = models.DateTimeField(auto_now=True) # автоматом при изменении

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"Advertisement(id={self.id}, title= {self.title}, price = {self.price})"

    # создаем новое отображение поля
    @admin.display(description="Дата создания")
    def created_date(self): # (новое название поля - created_date)
        from django.utils import timezone, html
        if self.created_at.date() == timezone.now().date(): # если дата создания объявления совпадает с нашей датой
            # сохраним время создания как строку
            created_time = self.created_at.time().strftime("%H:%M:%S")
            # возвращаем html код
            return html.format_html("<span style='color:green; font-style: italic; font-weight: bold;'>Сегодня в {}</span>", created_time)
        else:
            return self.created_at.strftime("%d:%m:%y в %H:%M:%S")
        

    


# # А что за скобки то ?
# class Human:
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight

#     def walk(self):
#         print("хожу")

# # наследование
# class Fireman(Human):
#     # отображение когда пишем print
#     def __str__(self):
#         return f"Человек, рост: {self.height}, вес: {self.weight}"


# fireman = Fireman(180, 82)
# fireman.walk()
# human = Human(180, 92)
# print(fireman)
# print(human)
