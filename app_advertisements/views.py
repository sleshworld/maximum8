from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

from django.shortcuts import redirect 
from django.urls import reverse

# Create your views here.
def main(request):
    # получаем все записи из БД
    adverts = Advertisement.objects.all()
    context = {"adverts": adverts}
    return render(request, "index.html", context=context)


def top_sellers(request):
    return render(request, "top-sellers.html")

def account(request):
    username = ""
    if request.method == "POST": # если метод запроса = POST (отправить)
        # получаем словарь с ключами = name в input и значениями, которые ввел пользователь
        d = request.POST
        username = d.get("username")
    context = {"username": username}
    return render(request, "account.html", context=context)

from .forms import AdvertisementForm
def advertisement_post(request):
    if request.method == "POST":
        # передаем в форму данные и файлы
        form = AdvertisementForm(request.POST, request.FILES)
        # проверяем правильность заполнения формы
        if form.is_valid():
            # создаем объявление согласно модели
            advertisement = Advertisement(**form.cleaned_data)
            # в форме нет выбора пользователя, мы получаем его из запроса
            advertisement.user = request.user
            advertisement.save()
            # создает ссылку для перехода на нужную страницу
            url = reverse("main")
            # делаем переход по этой ссылке
            return redirect(url)
    form = AdvertisementForm()
    context = {"form": form}
    return render(request, "advertisement-post.html", context=context)

def mini_game(request):
    
    import requests
    from bs4 import BeautifulSoup
    from datetime import datetime
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    date = datetime.today()
    date_str = date.strftime("%d/%m/%Y")

    params = {"date_req" : date_str}
    responce = requests.get(url=url, params=params)

    html = BeautifulSoup(responce.content, "html.parser")

    def getCourse(id):
        return html.find("valute", attrs={"id":id}).value.text.replace(",", ".")
    context = {"some_info": 123, 
    "valute": getCourse("R01235"), 
    "list": [1, 2, 3, 4]}
    return render(request, "mini_game.html", context=context)