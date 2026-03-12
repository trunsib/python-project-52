from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
    )
    password_confirm = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Пароли не совпадают")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    