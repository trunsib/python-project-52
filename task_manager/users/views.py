from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы залогинены")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def logout_view(request):
    logout(request)
    messages.success(request, "Вы разлогинены")
    return redirect('login')

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    
    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно изменён")
        return super().form_valid(form)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    
    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно удалён")
        return super().form_valid(form)
    