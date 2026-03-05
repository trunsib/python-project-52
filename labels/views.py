from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Label


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/list.html"
    context_object_name = "labels"


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ["name"]
    template_name = "labels/form.html"
    success_url = reverse_lazy("labels:index")

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ["name"]
    template_name = "labels/form.html"
    success_url = reverse_lazy("labels:index")

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно изменена")
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/confirm_delete.html"
    success_url = reverse_lazy("labels:index")

    def delete(self, request, *args, **kwargs):
        label = self.get_object()

        if label.task_set.exists():
            messages.error(request, "Нельзя удалить метку, потому что она используется")
            return redirect("labels:index")

        messages.success(request, "Метка успешно удалена")
        return super().delete(request, *args, **kwargs)
    