from django.contrib import admin
from .models import Advertisement # импортируем модель для работы с БД
# Register your models here.

# класс для управления моделью из админки
class AdvertisementAdmin(admin.ModelAdmin):
    # столбцы, которые будут отображаться
    list_display = ["id", "title", "description", "price", "user", "created_date", "auction", "updated_date", "show_image"]
    # список полей для фильтрации
    list_filter = ["auction", "created_at", "price"]
    # добавляем действие в отображение
    actions = ["make_auction_as_false", "make_auction_as_true"]
    # кстомизация полей ввода
    fieldsets = (
        ("Общее", { # подзаголовок
            "fields": ("title", "description", "image", "user") # поля внутри него
        }),
        ("Финансы", { # подзаголовок
            "fields": ("price", "auction"), # поля внутри него
            "classes": ["collapse"] # добавление класса (дизайна) для сворачивания и разворачивания
        })
    )

    # создаем действие, которое можно произвести с строчкой в таблице
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    



# соединяем класс и модель
admin.site.register(Advertisement, AdvertisementAdmin)