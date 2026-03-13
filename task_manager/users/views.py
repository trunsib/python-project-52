from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import UserCreateForm


class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/form.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/form.html"
    success_url = reverse_lazy("users:list")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно изменён")
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:list")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно удалён")
        return super().form_valid(form)


class LoginView(DjangoLoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        messages.success(self.request, "Вы залогинены")
        return super().form_valid(form)


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)
    