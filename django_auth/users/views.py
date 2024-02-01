from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.http import HttpResponse


# Создаем здесь представления.
def home(request):
    return render(request, "users/home.html")

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"




