from __future__ import unicode_literals

from django.db import models
from django import forms
from django.core.validators import RegexValidator, MinLengthValidator
from datetime import datetime
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


#METHOD 1: VALIDATING THE FORM USING THE FORM MANAGER
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 2:
            errors['first_name length'] = "First name must be at least 2 characters"
        if not postData['first_name'].isalpha():
            errors['first_name letters'] = "First name must only contain letters"

        if len(postData['last_name']) < 2:
            errors['last_name length'] = "Last name must be at least 2 characters"
        if not postData['last_name'].isalpha():
            errors['last_name letters'] = "First name must only contain letters"

        if datetime.strptime( postData['birthday'], '%Y-%m-%d').year > 2002:
            errors['age'] = "Must be over 16 to register"

            if datetime.strptime( postData['birthday'], '%Y-%m-%d').year > datetime.now().year:
                errors['date'] = "Please provide a valid date"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email address"
        
        if len(postData['pass']) < 8:
            errors['password'] = "Passwords must be at least 8 characters"
            if postData['pass'] != postData['passconf']:
                errors['password match'] = "Passwords must match"

        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[RegexValidator(regex='^[a-zA-Z]{2,}$', message='Field must be mimimum 2 characters and only letters', code='invalid_username'),])  
    last_name = models.CharField(max_length=255, validators=[RegexValidator(regex='^[a-zA-Z]{2,}$', message='Field must be mimimum 2 characters and only letters', code='invalid_username'),]) 
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(8)])
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()   

    def __str__(self):
        return self.email




#METHOD 2: USING A NORMAL FORM
class NameField(forms.Field):
    def validate(self, value):
        super(NameField, self).validate(value)
        if len(value) < 2:
            raise forms.ValidationError("Field must be at least 2 characters")
        if not value.isalpha():
            raise forms.ValidationError("Field must contain only letters")
            

class RegistrationForm(forms.Form):
    first_name = NameField()                                                          #validate this field by creating a custom field
    last_name = forms.CharField(min_length=2, validators=[RegexValidator(regex='^[a-zA-Z]*$', message='Field must contain only letters', code='invalid_username'),])  #validate this field using built-in validators
    email = forms.EmailField(label="Email", max_length=100)                           #validate this field using built-in validators
    birthday = forms.DateField()                                                      #validate this field using FIELD clean method
    password = forms.CharField(label="Password", min_length=8, max_length=100)        #validate this field using built-in validators
    passconf = forms.CharField(label="Confirm Password", max_length=100)              #validate this field using FORM clean method
    
    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        if data.year > 2002:
            self.add_error('birthday', "Must be over 16 to register")
        return data

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        passconf = cleaned_data.get('passconf')

        if password != passconf:
            self.add_error('passconf', "Passwords must match")

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
        




#METHOD 3: USING A MODEL FORM
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
