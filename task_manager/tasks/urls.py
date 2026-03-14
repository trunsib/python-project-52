from django.urls import path
from .views import RegisterView, login_view, logout_view, home

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/create/", RegisterView.as_view(), name="register"),
]
