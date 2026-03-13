from django import forms
from .models import Status, Label, Task

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ["name"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
        