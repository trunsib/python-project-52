from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Страница логина
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # перенаправление после успешного входа
    else:
        form = AuthenticationForm()
    return render(request, "tasks/login.html", {"form": form})


# Страница регистрации
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # после регистрации на страницу логина
    else:
        form = UserCreationForm()
    return render(request, "tasks/register.html", {"form": form})


# Страница выхода
def logout_view(request):
    logout(request)
    return redirect("login")
