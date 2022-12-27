from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


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
    title = 'Анфиса для друзей'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Какой-то текст',
        'list': [1, 2, 3]
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def post_num(request, pk):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'yatube/posts/post_num.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Анфиса для друзей'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Какой-то текст',
        'list': [1, 2, 3],
        'pk': pk,
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
def group_posts(request, slug):
    a = '''<!DOCTYPE html>
<html lang="ru">
  <head>
    <!-- Другие мета-теги тут -->
    <!-- Подключили адаптивность  -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Подключили CSS-файл Bootstrap -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
      crossorigin="anonymous">
    <!-- После стилевого файла Bootstrap можно
         написать собственные стили в теге <style> -->
    <!-- А лучше подключить свой CSS-файл и описать свои стили в нём:
        <link rel="stylesheet" href="css/style.css"> -->
    <style>
      .card {
        background: #eee;
        box-shadow: rgb(0 0 0 / 20%) 20px 20px 50px;
      }
    </style>
  </head>
  <body>

    <!-- Классы Bootstrap можно применять и к семантическим блокам. -->
    <div class="container">

      <!-- Начало глобального div.row с двумя колонками: 
       в левой колонке - имена авторов, в правой - блоки с текстом -->
      <div class="row">

        <!-- Начало левой колонки сайта со списком авторов -->
        <aside class="col-12 col-md-3">
          <ul class="list-group">
            <li class="list-group-item">Аксентий Поприщин</li>
            <li class="list-group-item">Робинзон Крузо</li>
            <li class="list-group-item">Чарли Гордон</li>
            <li class="list-group-item">Владимир Высоцкий</li>
          </ul>
        </aside>
        <!-- Конец левой колонки сайта -->

        <!-- Начало правой (широкой) колонки сайта -->
        <section class="col-12 col-md-9">

          <!-- Можно разбить на колонки содержимое любого блока.
           В этом div.row созданы четыре колонки с анонсами постов -->
          <div class="row">

            <!-- Начало первой колонки -->
            <article class="col-12 col-md-6 col-xl-6">
              <div class="card">
                <h5 class="card-header">Аксентий Поприщин</h5>
                <div class="card-body">
                  <h6 class="card-subtitle">Число 25</h6>
                  <p>
                    Сегодня великий инквизитор пришел в мою комнату, но я,
                    услышавши еще издали шаги его, спрятался под стул.
                  </p>
                  <a href="" class="btn btn-primary">Читать целиком</a>
                </div>
              </div>
            </article>
            <!-- Конец первой колонки -->

            <!-- Начало второй колонки -->
            <article class="col-12 col-md-6 col-xl-6">
              <div class="card">
                <h5 class="card-header">Робинзон Крузо</h5>
                <div class="card-body">
                  <h6 class="card-subtitle">25 октября 1659 года</h6>
                  <p>
                    Шквальный ветер сотрясал остров целую ночь,
                    а наутро я увидел, что наш корабль разнесло в щепки.
                  </p>
                  <a href="" class="btn btn-primary">Читать целиком</a>
                </div>
              </div>
            </article>
            <!-- Конец второй колонки -->

            <!-- Начало третьей колонки -->
            <article class=" col-12 col-md-6 col-xl-6">
              <div class="card">
                <h5 class=" card-header">Чарли Гордон</h5>
                <div class="card-body">
                  <h6 class="card-subtitle">1 атчет 3 марта</h6>
                  <p>
                    Док Штраус сказал што я должен писать все што я думаю и
                    помню и все што случаеца со мной с севодня. Я не знаю
                    пачему но он гаварит што это важно штобы они могли
                    увидить што я падхажу им.
                  </p>
                  <a href="" class="btn btn-primary">Читать целиком</a>
                </div>
              </div>
            </article>
            <!-- Конец третьей колонки -->

            <!-- Начало четвёртой колонки -->
            <article class=" col-12 col-md-6 col-xl-6">
              <div class="card">
                <h5 class=" card-header">Владимир Высоцкий</h5>
                <div class="card-body">
                  <h6 class="card-subtitle">3 апреля 1976 года</h6>
                  <p>
                    Если б Кащенко, к примеру, лёг лечиться к Пирогову -
                    Пирогов бы без причины резать Кащенку не стал…
                  </p>
                  <a href="" class="btn btn-primary">Читать целиком</a>
                </div>
              </div>
            </article>
            <!-- Конец четвёртой колонки -->
          </div>  <!-- Конец вложенного div.row -->

        </section>  <!-- Конец правой (широкой) колонки сайта -->
      </div>  <!-- Конец div.row  -->
    </div>  <!-- Конец div.container -->
  </body>
</html>'''
    return HttpResponse(a)
