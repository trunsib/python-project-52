from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('create/', views.register, name='user_create'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]
