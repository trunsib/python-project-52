from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

# CRUD пользователей
class UserListView(ListView):
    model = User
    template_name = 'users/list.html'

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name = 'users/form.html'
    success_url = reverse_lazy('users:login')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email']
    template_name = 'users/form.html'
    success_url = reverse_lazy('users:list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/confirm_delete.html'
    success_url = reverse_lazy('users:list')

# Вход/выход
class LoginView(DjangoLoginView):
    template_name = 'users/login.html'

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('users:login')
    