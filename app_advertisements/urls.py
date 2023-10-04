from django.urls import path

from .views import main, top_sellers, mini_game

urlpatterns = [
    path("", main, name = "main"),
    path("top-sellers/", top_sellers, name = "top-sellers"),
    path("mini-game/", mini_game, name = "mini-game")
]