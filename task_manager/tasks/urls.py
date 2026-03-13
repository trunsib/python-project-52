from django.urls import path
from . import views

urlpatterns = [
    path("users/create/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
]
