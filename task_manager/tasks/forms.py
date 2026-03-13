from django import forms
from .models import Status, Label, Task


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]  # поле в модели Status


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ["name", "description"]  # поля модели Label


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
        