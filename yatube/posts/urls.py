# yatube/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('posts/group_list.html', views.group_list, name='group_list'),
    # path('group/<slug:slug>', views.group_posts),
    path('posts/', views.posts, name='posts'),
    path('post/<pk>', views.post_num, name='post')
    # Страница со списком сортов мороженого
    # path('ice_cream/', views.ice_cream_list),
    # Отдельная страница с информацией о сорте мороженого
    # path('ice_cream/<pk>/', views.ice_cream_detail),
]