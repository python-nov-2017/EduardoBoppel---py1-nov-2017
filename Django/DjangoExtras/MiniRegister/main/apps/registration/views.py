from django.shortcuts import render, redirect
from forms import UserForm, LoginForm
from django.core.urlresolvers import reverse
from .models import User
import bcrypt

def index(request):
    regform = UserForm()
    loginform = LoginForm()
    context = {
        'regform': regform,
        'loginform': loginform
    }
    return render(request, 'registration/index.html', context)

def register(request):
    regform = UserForm(request.POST)
    if regform.is_valid():
        regform.createuser()
        request.session['email'] = request.POST['email']
        return redirect(reverse('registration:success'))
    
    else:
        loginform = LoginForm()
        context = {
            'regform': regform,
            'loginform': loginform
        }
        return render(request, 'registration/index.html', context)



def login(request):
    loginform = LoginForm(request.POST)
    if loginform.is_valid():
        request.session['email'] = request.POST['email']
        return redirect(reverse('registration:success'))
    else:
        regform = UserForm()
        context = {
            'regform': regform,
            'loginform': loginform
        }
        return render(request, 'registration/index.html', context)


def logout(request):
    del request.session['email']
    return redirect(reverse('registration:index'))


def success(request):
    user = User.objects.get(email=request.session['email'])
    return render(request, 'registration/success.html', {'user':user})