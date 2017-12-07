from __future__ import unicode_literals

from django.db import models
from django import forms
from django.core.validators import RegexValidator, MinLengthValidator
from datetime import datetime
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[RegexValidator(regex='^[a-zA-Z]{2,}$', message='Field must be mimimum 2 characters and only letters', code='invalid_username'),])  
    last_name = models.CharField(max_length=255, validators=[RegexValidator(regex='^[a-zA-Z]{2,}$', message='Field must be mimimum 2 characters and only letters', code='invalid_username'),]) 
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email



class UserForm(forms.ModelForm):    
    passconfirm = forms.CharField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'birthday', 'password' ]

    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        if data.year > 2002:
            self.add_error('birthday', "Must be over 16 to register")
        return data

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        print cleaned_data.get('password')
        print cleaned_data.get('passconfirm')

        if cleaned_data.get('password') != cleaned_data.get('passconfirm'):
            print "passwords dont match"
            self.add_error('passconfirm', "Passwords must match")



class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", max_length=100)

    def clean(self):       
        cleaned_data = super(LoginForm,self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        try:
            user = User.objects.get(email=email)
        except: 
            self.add_error('email', "Please enter a valid registered email")
        else:
            if not bcrypt.checkpw('password'.encode(), user.password.encode()):
                self.add_error('password', "Please entere a valid password")


