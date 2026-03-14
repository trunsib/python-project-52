from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('login')

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
