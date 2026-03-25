from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы залогинены")
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
    