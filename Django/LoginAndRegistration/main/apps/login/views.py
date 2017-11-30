from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.forms import modelform_factory
import bcrypt
from models import *


def index(request):
    if 'user_id' in request.session:
        return redirect('/home')
    
    #####THIS IS FOR METHOD 2: NORMAL FORM######
    regform = RegistrationForm()
    loginform = LoginForm()

    #####THIS IS FOR METHOD 3: MODELFORM ######
    userform = UserForm()                              
    return render(request, 'login/index.html', {'regform': regform, 'loginform': loginform, 'userform': userform })

def home(request):
    if 'user_id' in request.session:
        return render(request, 'login/home.html')
    return redirect('/')

def logout(request):
    del request.session['user_id']
    return redirect('/')



#### METHOD 1: HTML FORM AND MODEL MANAGER AND FLASH MESSAGES
def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == dict:
        for tag, error in result.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/')
    request.session['user_id'] = result.id  
    return redirect('/home')


def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == dict:
        for tag, error in result.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/')
    request.session['user_id'] = result.id  
    return redirect('/home')





#### METHOD 2: NORMAL FORM:
def registernormalform(request):
    regform = RegistrationForm(request.POST)

    if regform.is_valid():
        hashpass = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        User.objects.create(first_name=regform.cleaned_data['first_name'],
                            last_name=regform.cleaned_data['last_name'],
                            email=regform.cleaned_data['email'],
                            birthday=regform.cleaned_data['birthday'],
                            password=regform.cleaned_data['password'])
    
        request.session['user_id'] = regform.cleaned_data['email']
        return redirect('/home')

    return render(request, 'login/index.html', {'regform': regform, 'loginform': LoginForm(),'userform': UserForm() })

def loginnormalform(request):
    loginform = LoginForm(request.POST)

    if loginform.is_valid():
        user = User.objects.get(email=loginform.cleaned_data['email'])
        request.session['user_id'] = user.email
        return redirect('/home')

    return render(request, 'login/index.html', {'regform': RegistrationForm(), 'loginform': LoginForm(), 'userform': UserForm() })




#### METHOD 3: MODEL FORM:
def registermodelform(request):
    userform = UserForm(request.POST)
    
    if userform.is_valid():
        userform.save()
        request.session['user_id'] = userform.cleaned_data['email']
        return redirect('/home')
    
    return render(request, 'login/index.html', {'regform': RegistrationForm(), 'loginform': LoginForm(), 'userform': userform })

