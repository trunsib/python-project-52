from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('task_manager.tasks.urls')),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('login/', RedirectView.as_view(url='/users/login/', permanent=False), name='login'),
    path('admin/', admin.site.urls),
]
