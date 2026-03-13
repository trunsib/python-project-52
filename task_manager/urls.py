from django.contrib import admin
from django.urls import path, include
from task_manager.tasks import views as task_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", task_views.home, name="home"),

    path("users/login/", task_views.login_view, name="login"),
    path("users/logout/", task_views.logout_view, name="logout"),
    path("users/create/", task_views.register_view, name="register"),

    path("tasks/", include("task_manager.tasks.urls")),
]
