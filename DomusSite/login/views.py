from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView


def login(request):
    return render(request, 'login/login.html')






class CustomLoginView(LoginView):
    def form_valid(self, form):
        # Здесь вызывается при успешной валидации формы входа
        messages.success(self.request, 'Вы успешно вошли!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # Здесь вызывается при ошибке валидации формы входа
        messages.error(self.request, 'Ошибка входа. Пожалуйста, проверьте данные.')
        return super().form_invalid(form)
