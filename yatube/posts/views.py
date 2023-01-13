from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from datetime import date
from .models import Post, Group

# Главная страница
'''
def index(request):
    # Загружаем шаблон;
    # шаблоны обычно хранят в отдельной директории.
    template = loader.get_template('yatube/index.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request))
'''


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'yatube/posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Тестовое приложение'
    posts = Post.objects.all()[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Какой-то текст',
        'list': [1, 2, 3],
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def post_num(request, pk):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'yatube/posts/post_num.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Выбор постов'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Вчера Крокодил<br>улыбнулся так злобно,<br>Что мне до сих '
                'пор<br>за него неудобно.<br><i>Рената Муха</i>',
        'list': [1, 2, 3],
        'pk': pk,
        'date': date.fromisoformat('2019-12-04'),

    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def group_list(request):
    template = loader.get_template('yatube/posts/group_list.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request))


'''def base(request):
    template = loader.get_template('yatube/base.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request))
'''


def posts(request):
    template = loader.get_template('yatube/posts/posts.html')
    # Формируем шаблон
    return HttpResponse(template.render({}, request))


# group posts
def group_posts(request, gr_num):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=gr_num)
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = group.posts.all()[:10]
    # posts = Post.objects.filter(group=group).all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'yatube/posts/group_list.html', context)
