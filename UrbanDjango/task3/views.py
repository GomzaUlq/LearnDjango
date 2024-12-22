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
    return render(request, 'home.html', context)


def magazine(request):
    tea = 'Чай'
    tea_1 = 'Пуэр'
    tea_2 = 'Да Хун Пао'
    tea_3 = 'Те Гуань Инь'
    buy = 'Купить'
    context = {
        'tea': tea,
        'tea_1': tea_1,
        'tea_2': tea_2,
        'tea_3': tea_3,
        'buy': buy,
    }
    return render(request, 'tea.html', context)


def cart(request):
    title = 'Вы еще не добавили товар'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)
