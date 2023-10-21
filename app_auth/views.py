from django.shortcuts import render, redirect, reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
def login_view(request):
    # если запрос гет 
    if request.method == "GET":
        # проверяем авторизован ли пользователь
        if request.user.is_authenticated:
            # если да, редиректим на страницу профиля
            return redirect(reverse("profile"))
        else:
            # если нет, отображаем страницу входа
            return render(request, "app_auth/login.html")
    # если не гет запрос, то считаем, что POST

    # получаем введеный username
    username = request.POST["username"]
    # получаем введенный пароль
    password = request.POST["password"]
    # производим вход
    user = authenticate(request, username=username, password=password)
    # если вход проищозошел - получили пользователь (не None)
    if user is not None:
        # говорим, что пользователь вошел
        login(request, user)
        # редиректим на страницу профиля
        return redirect(reverse("profile"))
    # если None - не нашли пользователя
        # отображаем страницу с логином и дополнительно пишем ошибкуЮ переданную через контекст
    return render(request, "app_auth/login.html", context={"error": "Пользователь не найден"})

def logout_view(request):
    logout(request)
    return redirect(reverse("login"))
    
@login_required(login_url=reverse_lazy("login"))
def profile_view(request):
    return render(request, "app_auth/profile.html")
# импортируем класс формы
from .forms import RegisterForm
def register(request):
    # если пришел пост запрос (не гет)
    if request.method == "POST":
        # в форму закидываем отправленные данные
        form = RegisterForm(request.POST)
        # проверяем на валидность
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("profile"))
    else:
        form = RegisterForm()
    return render(request, "app_auth/register.html", context = {"form": form})