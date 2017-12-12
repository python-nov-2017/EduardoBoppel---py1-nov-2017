from django import forms
from .models import User
import bcrypt



class UserForm(forms.ModelForm):
    passconfirm = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'passconfirm']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        if not cleaned_data.get('password') == cleaned_data.get('passconfirm'):
            self.add_error('passconfirm', "Passwords must match")

    def createuser(self):
        newuser = self.save(commit=False)
        password = self['password'].value()
        hashpwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        newuser.password = hashpwd
        newuser.save()


class LoginForm(forms.Form):
    email = forms.CharField(max_length = 255)
    password = forms.CharField(max_length = 255)

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        
        try:
            user = User.objects.get(email=email)
        except:
            self.add_error("email", "Please enter a valid registered email")
        else:
            print password
            print user.password

            if not bcrypt.checkpw(password.encode(), user.password.encode()):
                print "passwords do not match"
                self.add_error('password', "Please enter a valid password")
