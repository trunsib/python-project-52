import django_filters
from django import forms
from django.contrib.auth import get_user_model

from .models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label

User = get_user_model()


class TaskFilter(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Статус"
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Исполнитель"
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка"
    )

    self_tasks = django_filters.BooleanFilter(
        label="Только свои задачи",
        method="filter_self_tasks",
        widget=forms.CheckboxInput
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
    