# yatube/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/<slug:slug>', views.group_posts)
    # Страница со списком сортов мороженого
    # path('ice_cream/', views.ice_cream_list),
    # Отдельная страница с информацией о сорте мороженого
    # path('ice_cream/<pk>/', views.ice_cream_detail),
]