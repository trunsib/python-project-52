from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from task_manager.statuses.models import Status


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
    
    def get_queryset(self):
        return Status.objects.all()


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if Status.objects.filter(name=name).exists():
            messages.error(self.request, "Статус с таким именем уже существует")
            return self.form_invalid(form)
        
        messages.success(self.request, "Статус успешно создан")
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    
    def form_valid(self, form):
        messages.success(self.request, "Статус успешно изменен")
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    
    def form_valid(self, form):
        if self.object.task_set.exists():
            messages.error(
                self.request,
                "Невозможно удалить статус, который используется в задаче"
                )
            return redirect('statuses')
        messages.success(self.request, "Статус успешно удален")
        return super().form_valid(form)
    