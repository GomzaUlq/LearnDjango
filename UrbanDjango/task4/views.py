from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def home(request):
    title = 'Главная страница'
    home_page = 'Главная'
    magazine_tea = 'Магазин'
    product_cart = 'Корзина'
    context = {
        'title': title,
        'home_page': home_page,
        'magazine_tea': magazine_tea,
        'product_cart': product_cart,

    }
    return render(request, 'menu.html', context)


def magazine(request):
    tea = 'Чай'
    buy = 'Купить'
    context = {
        'tea': tea,
        'tea_all': ["Пуэр", "Да Хун Пао", "Те Гуань Инь"],
        'buy': buy,
    }
    return render(request, 'tea.html', context)


def cart(request):
    title = 'Вы еще не добавили товар'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)
