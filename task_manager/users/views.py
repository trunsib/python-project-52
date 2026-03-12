from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django import forms


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Логин',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('users:login')


class UserUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'users/form.html'
    success_url = reverse_lazy('users:list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/confirm_delete.html'
    success_url = reverse_lazy('users:list')


class LoginView(DjangoLoginView):
    template_name = 'users/login.html'


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('users:login')
    