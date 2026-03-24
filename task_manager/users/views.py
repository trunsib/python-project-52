from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect('login')
        else:
            print("From errors:", form.errors)
            messages.error(request, "Пожалуйста, исправте ошибки в форме")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
