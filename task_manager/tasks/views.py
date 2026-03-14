from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


def home(request):
    return render(request, "home.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "tasks/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
    