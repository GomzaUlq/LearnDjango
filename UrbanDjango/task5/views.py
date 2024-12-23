from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Alex', 'Vasya', 'Urban']


# Create your views here.
def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        print(username)
        if password == repeat_password and int(age) >= 18 and username not in users:
            users.append(username)
            print(users)
            return HttpResponse(f'Приветствуем, {username}!"')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        if int(age) < 18:
            info['error'] = ('Вы должны быть старше 18')
        if username in users:
            info['error'] = ('Пользователь с таким именем уже существует')

    return render(request, 'fifth_task/registrarion_page.html', context=info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(username)
            if password == repeat_password and int(age) >= 18 and username not in users:
                users.append(username)
                print(users)
                return HttpResponse(f'Приветствуем, {username}!"')
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if int(age) < 18:
                info['error'] = ('Вы должны быть старше 18')
            if username in users:
                info['error'] = ('Пользователь с таким именем уже существует')
        else:
            form = UserRegister()
    return render(request, 'fifth_task/registrarion_page.html', {'form': info})
