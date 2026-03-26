from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth.models import User
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


def home(request):
    """Главная страница"""
    return render(request, 'home.html')


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.all().select_related(
            'status',
            'author',
            'executor'
            ).prefetch_related(
                'labels'
                )


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if Task.objects.filter(name=name).exists():
            messages.error(self.request, "Задача с таким именем уже существует")
            return self.form_invalid(form)
        
        form.instance.author = self.request.user
        messages.success(self.request, "Задача успешно создана")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['users'] = User.objects.all()
        context['labels'] = Label.objects.all()
        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "Задача успешно изменена")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['users'] = User.objects.all()
        context['labels'] = Label.objects.all()
        return context


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    
    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user
    
    def handle_no_permission(self):
        messages.error(self.request, "Задачу может удалить только ее автор")
        return redirect('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "Задача успешно удалена")
        return super().form_valid(form)
    