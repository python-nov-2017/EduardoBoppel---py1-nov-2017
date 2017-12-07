from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.forms import modelform_factory
from django.core.urlresolvers import reverse
import bcrypt
from models import *


def index(request):
    if 'user_id' in request.session:
        return redirect(reverse('login:home'))
    
    userform = UserForm()                              
    loginform = LoginForm()
    
    return render(request, 'login/index.html', {'loginform': loginform, 'userform': userform })

def home(request):
    if 'user_id' in request.session:
        return render(request, 'login/home.html')
    return redirect(reverse('login:index'))

def logout(request):
    del request.session['user_id']
    return redirect(reverse('login:index'))



def registermodelform(request):
    userform = UserForm(request.POST)
    
    if userform.is_valid():
        userform.save()
        request.session['user_id'] = userform.cleaned_data['email']
        return redirect('/home')
    
    return render(request, 'login/index.html', {'regform': RegistrationForm(), 'loginform': LoginForm(), 'userform': userform })


def loginnormalform(request):
    loginform = LoginForm(request.POST)

    if loginform.is_valid():
        user = User.objects.get(email=loginform.cleaned_data['email'])
        request.session['user_id'] = user.email
        return redirect(reverse('login:home'))

    return render(request, 'login/index.html', {'regform': RegistrationForm(), 'loginform': LoginForm(), 'userform': UserForm() })





########### USERS
def users(request):
    return render(request, 'login/users.html', {'users': User.objects.all() } )

def adduser(request):
    form = UserForm()
    return render(request, 'login/newuser.html', {'form': form} )

def updateuser(request, id=None):
    if id:
        user = User.objects.get(id=id)
        form = UserForm(request.POST, instance=user)
    else: 
        form = UserForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/users')
    else:
        print "errors"
        return redirect('/login/adduser')

def showuser(request, id):
    return render(request, 'login/showuser.html', {'user':User.objects.get(id=id) })

def edituser(request, id):
    user = User.objects.get(id=id)
    form = UserForm(instance=user)
    return render(request, 'login/newuser.html', {'form': form, 'id': user.id} )

def deleteuser(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')


