from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('task_manager.tasks.urls')),
    path('users/', include('task_manager.users.urls')),
    path('admin/', admin.site.urls),
]
