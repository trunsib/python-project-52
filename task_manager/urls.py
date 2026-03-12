from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('task_manager.index_urls')),

    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('statuses/', include('task_manager.statuses_urls')),
    path('labels/', include('task_manager.labels_urls')),
    path('tasks/', include('task_manager.tasks_urls')),
]
