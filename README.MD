# Booklibraryapp

## О проекте
Проект написан на Django Framework v2.2.7
Для API использован Django Rest Framework v3.11.0
## Быстрый старт
Вам нужен Python 3.6 и выше.

git clone https://github.com/WhiteJamer/dealerapp
В репозитории:

pip install -r requirements.txt
Выберите базу данных и запустите:

manage.py makemigrations
manage.py migrate
Создайте суперюзера:

manage.py createsuperuser
Запустите дев-сервер:

manage.py runserver
API документация:
### Книги:
Получить все книги - GET /api/books/

Получить информацию о конкретной книге - GET /api/books/{ID}/
Поставить оценку книге - GET /api/books/{ID}/vote/

### Литераторы:
Получить всех литераторов - GET /api/literators/

Получить информацию о конкретном литераторе - GET /api/literators/{ID}/
![0724921529c74c883acb3c5389461c0b.png](https://picua.org/images/2020/02/10/0724921529c74c883acb3c5389461c0b.png)
