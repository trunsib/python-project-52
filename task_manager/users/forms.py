from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя', 
        max_length=150,
        required=True
    )
    last_name = forms.CharField(
        label='Фамилия', 
        max_length=150,
        required=True
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        