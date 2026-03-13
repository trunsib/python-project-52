from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # маршруты приложения tasks
    path('tasks/', include('tasks.urls')),

    # маршруты аутентификации
    path('register/', task_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
