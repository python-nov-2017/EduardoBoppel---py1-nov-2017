from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserRegistrationForm

class UserRegistration(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user_form.html'
    success_url = '/'


class ListUsers(ListView):
    model = User    
    context_object_name = 'users'


class UserDetail(DetailView):
    model = User
    context_object_name = 'users'


class UserCreate(CreateView):
    model = User
    fields = ['email', 'first_name', 'last_name', 'description', 'is_staff', 'is_admin']


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'description']


class UserDelete(DeleteView):
    model = User
    context_object_name = 'user'
    template_name = 'accounts/confirm_delete.html'
    success_url = reverse_lazy('accounts:user_list')

    
    
