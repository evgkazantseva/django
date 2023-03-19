from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
user_data = {
    "name": "Иван",
    "middlename": "Петрович",
    "surname": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def index(request):
    return HttpResponse(f"<h1>Изучаем django </h1><strong> Автор </strong>: <i> Казанцева Е.А. </i>")


def about(request):
    return HttpResponse(f"<p><strong>Фамилия:</strong>{user_data['surname']}</p>"
                        f"<p><strong>Имя:</strong> {user_data['name']}</p>"
                        f"<p><strong>Отчество:</strong> {user_data['middlename']}</p>"
                        f"<p><strong>Телефон:</strong> {user_data['phone']}</p>"
                        f"<p><strong>Email:</strong> {user_data['email']}</p>")


def item(request, item_id):
    for item_el in items:
        if item_id == int(item_el['id']):
            return HttpResponse(f"<p><strong>Название товара:</strong>{item_el['id']}:{item_el['name']}</p>"
                                f"<p><strong>Количество товара:</strong> {item_el['quantity']}</p>"
                                f"<p><a href='/items'>Вернуться назад</a><p>")
    return HttpResponse(f"<h4>Товар с id={item_id} не найден<h4>"
                                f"<p><a href='/items'>Вернуться назад</a><p>")


def items_list(request):
    html = "<ol>"
    for i in range(len(items)):
        html += f"<li><a href='/item/{items[i]['id']}'>{items[i]['name']}</a></li>"
    html += "</ol>"
    return HttpResponse(html)
