from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import Status, Label, Task
from .forms import StatusForm, LabelForm, TaskForm


class StatusCreateView(CreateView):
    model = Status
    form_class = StatusForm
    template_name = "tasks/form.html"
    success_url = "/statuses/"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Статус успешно создан")
        return super().form_valid(form)


class LabelCreateView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = "tasks/form.html"
    success_url = "/labels/"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/form.html"
    success_url = "/tasks/"

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Задача успешно создана")
        return super().form_valid(form)
    