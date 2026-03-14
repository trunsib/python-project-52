from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, "Пользователь успешно зарегистрирован")
            
            return redirect("/login/")

    else:
        form = UserCreationForm()

    return render(request, "users/create.html", {"form": form})
