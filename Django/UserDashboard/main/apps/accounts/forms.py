from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        # extra: set user.active to false, send email, and validate user
        if commit:
            user.save()
        return user