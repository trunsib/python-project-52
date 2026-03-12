from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView


class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    template_name = "users/form.html"
    fields = ["first_name", "last_name", "username", "password"]
    success_url = reverse_lazy("users:list")


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/form.html"
    fields = ["first_name", "last_name", "username"]
    success_url = reverse_lazy("users:list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:list")


class UserLoginView(LoginView):
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("index")
    