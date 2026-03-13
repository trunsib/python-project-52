from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views as task_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path('', include('task_manager.tasks.urls')),
    path("tasks/", include("tasks.urls")),
    path('register/', task_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
