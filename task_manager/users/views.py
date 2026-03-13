from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreateForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/form.html"
    success_url = reverse_lazy("login")  # редирект после регистрации

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)
    