from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import UserCreationForm


def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()

    return render(request, 'users/form.html', {'form': form})
