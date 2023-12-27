from django.urls import path
from django.contrib.auth import views as auth_views



urlpatterns = [
    # Другие URL-адреса вашего приложения, если они есть
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login')
    # Другие URL-адреса вашего приложения
]