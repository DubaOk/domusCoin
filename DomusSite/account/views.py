from django.shortcuts import render
def account(request):
 return render(request, 'account/accaunt.html')



def profile_view(request):
    user = request.user

    # Если пользователь аутентифицирован, можно получить его данные
    if user.is_authenticated:
        username = user.username
        email = user.email
        # Другие данные пользователя, если нужно

        return render(request, 'account/accaunt.html', {'username': username, 'email': email})
    else:
        # Логика для неаутентифицированных пользователей
        return render(request, 'login/login.html', {})