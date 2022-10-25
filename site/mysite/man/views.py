from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    return HttpResponse("Мужицкая страница")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")