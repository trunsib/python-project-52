from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def create(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect("/login/")
    else:
        form = UserCreationForm()

    return render(request, "users/form.html", {"form": form})
