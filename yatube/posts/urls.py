# yatube/urls.py
from django.urls import path


from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    path('posts/group_list.html', views.group_list, name='group_list'),
    # path('group/<slug:slug>', views.group_posts),
    path('posts/', views.posts, name='posts'),
    path('post/<int:pk>', views.post_num, name='post'),
    path('group/<slug:gr_num>', views.group_posts, name='group')
]
