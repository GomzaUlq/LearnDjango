from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['Alex', 'Vasya', 'Urban']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if int(password) == int(repeat_password) and int(age) >= 18 and username != username:
            users.append(username)
            print(users)
            return HttpResponse(f'Приветствуем, {username}!"')
        elif int(password) != int(repeat_password):
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            return HttpResponse('Вы должны быть старше 18')

    return render(request, 'registrarion_page.html', {'form': info})


def sign_up_by_django(request):
    users = ['Alex', 'Vasya', 'Urban']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            return HttpResponse(f'Приветствуем, {username}!"')
    else:
        form = UserRegister()
    return render(request, 'registrarion_page.html', {'form': info})
