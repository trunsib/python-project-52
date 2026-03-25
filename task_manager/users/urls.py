from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('create/', views.register, name='user_create'),
]
