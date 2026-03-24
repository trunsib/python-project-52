from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from ..forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
