from django.urls import path

from .views import main, top_sellers, mini_game, account, advertisement_post, advertisement_detail

urlpatterns = [
    path("", main, name = "main"),
    path("top-sellers/", top_sellers, name = "top-sellers"),
    path("mini-game/", mini_game, name = "mini-game"),
    path("acc/", account),
    path("advertisement-post/", advertisement_post, name="adv-post"),
    path("advertisement/<int:pk>", advertisement_detail, name="adv-detail")
]