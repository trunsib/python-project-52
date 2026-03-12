from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Имя",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'})
    )
    last_name = forms.CharField(
        label="Фамилия",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'})
    )
    username = forms.CharField(
        label="Имя пользователя",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
    )
    password_confirm = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Имя пользователя уже занято")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Пароли не совпадают")
        return cleaned_data
    