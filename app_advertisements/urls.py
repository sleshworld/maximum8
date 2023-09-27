from django.urls import path

from .views import main, top_sellers

urlpatterns = [
    path("", main, name = "main"),
    path("top-sellers/", top_sellers, name = "top-sellers")
]