from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("passwordConfirm", "")

        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return render(request, "users/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "users/register.html")

        User.objects.create_user(username=username, password=password)
        return redirect("login")  # предполагается, что есть login view

    return render(request, "users/register.html")
