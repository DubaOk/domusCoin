from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/index.html')

def login(request):
    # Ваш код для обработки входа пользователя
    return render(request, '/login.html')






