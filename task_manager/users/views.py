from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib import messages

from .forms import UserRegisterForm


class UserListView(ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/form.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        messages.success(
            self.request,
            "Пользователь успешно зарегистрирован"
        )

        return response


class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "username"]
    template_name = "users/form.html"
    success_url = reverse_lazy("users:list")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Пользователь успешно изменён"
        )
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    template_name = "users/confirm_delete.html"
    success_url = reverse_lazy("users:list")

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            "Пользователь успешно удалён"
        )
        return super().delete(request, *args, **kwargs)


class LoginView(DjangoLoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        messages.success(
            self.request,
            "Вы залогинены"
        )
        return super().form_valid(form)


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("index")
    