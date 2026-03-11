from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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
    