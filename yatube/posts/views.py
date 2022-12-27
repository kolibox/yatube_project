from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# group posts
def group_posts(request, slug):
    return HttpResponse(f'Посты группы "{slug}"')
