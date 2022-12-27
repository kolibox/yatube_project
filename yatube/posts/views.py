from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# group posts
def group_posts(request, slug):
    a = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Краткое описание страницы">
    <title>Заголовок для отображения в названии вкладки</title>
    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
  </head>
  <body>
    <header>
        Верхняя часть страницы: логотип, контакты
      <nav>
        Меню (навигация)
      </nav>
    </header>
    <main>
      <div>
  <h5>Аксентий Поприщин</h5>
  <div>
    <h6>43 апреля 2000 года</h6>
    <p>
      Сегодняшний день — есть день величайшего торжества!
      В Испании есть король. Он отыскался. Этот король я.
      Именно только сегодня об этом узнал я.
    </p>
    <a class="btn btn-danger" href="">Читать целиком</a>
    <button type="button" class="btn btn-primary">Primary</button>
  </div>
</div>
    </main>
    <footer>
      Подвал
    </footer>
  </body>
</html>  '''
    return HttpResponse(a)
