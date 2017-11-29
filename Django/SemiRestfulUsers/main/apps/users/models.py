from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']