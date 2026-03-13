from django.urls import path
from .views import StatusCreateView, LabelCreateView, TaskCreateView

urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="task_create"),
]
