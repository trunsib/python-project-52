# task_manager/users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.register, name='user_create'),
    # позже добавьте другие URL для пользователей:
    # path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    # path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    # path('', views.UserListView.as_view(), name='user_list'),
]
