from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic import ListView
from django.contrib.auth.models import User

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect('login')
        else:
            print("=" * 50)
            print("REGISTRATION FORM ERRORS:")
            print(f"Form data: {request.POST}")
            for field, errors in form.errors.items():
                print(f"{field}: {', '.join(errors)}")
            print("=" * 50)
            messages.error(request, "Пожалуйста, исправьте ошибки в форме")
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
