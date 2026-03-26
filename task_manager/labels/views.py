from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from task_manager.labels.models import Label


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'
    
    def get_queryset(self):
        return Label.objects.all()


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if Label.objects.filter(name=name).exists():
            messages.error(self.request, "Метка с таким именем уже существует")
            return self.form_invalid(form)
        
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    
    def form_valid(self, form):
        messages.success(self.request, "Метка успешно изменена")
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    
    def form_valid(self, form):
        if self.object.task_set.exists():
            messages.error(
                self.request,
                "Невозможно удалить метку, которая используется в задаче"
                )
            return redirect('labels')
        messages.success(self.request, "Метка успешно удалена")
        return super().form_valid(form)
    