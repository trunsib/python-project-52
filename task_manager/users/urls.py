# task_manager/users/urls.py
from django.urls import path
from . import views

# Название namespace для ссылок
app_name = "users"

urlpatterns = [
    path("", views.UserListView.as_view(), name="index"),      # список пользователей
    path("login/", views.LoginView.as_view(), name="login"),   # вход
    path("logout/", views.LogoutView.as_view(), name="logout"),# выход
    path("create/", views.UserCreateView.as_view(), name="create"), # регистрация
]
