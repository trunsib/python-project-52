from django.contrib import admin
from django.urls import path, include
from task_manager.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    # главная страница
    path('', IndexView.as_view(), name='index'),

    # приложения
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]
