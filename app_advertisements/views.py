from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, "index.html")


def top_sellers(request):
    return render(request, "top-sellers.html")

def mini_game(request):
    return render(request, "mini_game.html")