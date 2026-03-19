from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
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

    return render(request, 'users/create.html', {'form': form})
