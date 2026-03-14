from django.contrib import admin
from django.urls import path, include
from task_manager.tasks import views as task_views
from task_manager.tasks.views import RegisterView, login_view, logout_view, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/create/', RegisterView.as_view(), name='register'),
    path('admin/', admin.site.urls),
]
