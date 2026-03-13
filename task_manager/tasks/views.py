from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# --- Вход ---
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # после входа на главную
        else:
            messages.error(request, "Неправильное имя пользователя или пароль")
    return render(request, "tasks/login.html")

# --- Регистрация ---
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Имя пользователя уже занято")
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            login(request, user)
            return redirect("/")  # после регистрации на главную
    return render(request, "tasks/register.html")
