from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('task_manager.tasks.urls')),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('statuses.urls')),
    path('labels/', include('labels.urls')),
    path('admin/', admin.site.urls),
]
