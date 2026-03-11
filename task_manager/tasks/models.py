from django.db import models
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")

    status = models.ForeignKey(
        "statuses.Status",
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Статус",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="author_tasks",
        verbose_name="Автор",
    )

    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="executor_tasks",
        verbose_name="Исполнитель",
        blank=True,
        null=True,
    )

    labels = models.ManyToManyField(
        Label,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    