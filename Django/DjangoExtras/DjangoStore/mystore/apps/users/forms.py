from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         self.fields.pop('username')

#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'password' ]



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name' ]

    def clean_password2(self):
        password1 = self.cleand_data.get('password1')        
        password2 = self.cleand_data.get('password2')        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2
        
        
    def save(self, commit=True):    
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        #set user.active to false, send email, and validate user
        if commit:
            user.save()
        return user
