from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.forms import modelform_factory
import bcrypt
from models import *


def index(request):
    if 'email' in request.session:
        return redirect('/home')
    
    #####THIS IS FOR METHOD 2: NORMAL FORM######
    regform = RegistrationForm()
    loginform = LoginForm()

    #####THIS IS FOR METHOD 3: MODELFORM ######
    userform = UserForm()                                                   #using the class method

    return render(request, 'login/index.html', {'regform': regform, 'loginform': loginform, 'userform': userform })

def home(request):
    if 'email' in request.session:
        return render(request, 'login/home.html')
    return redirect('/')

def logout(request):
    del request.session['email']
    return redirect('/')



#### METHOD 1: HTML FORM AND MODEL MANAGER AND FLASH MESSAGES
def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect ('/')

    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        birthday = request.POST['birthday']
        password = request.POST['pass']
        hashpass = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        User.objects.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=hashpass)
        request.session['email'] = email
        return redirect('/home')
    return redirect('/')


def login(request):
    try:
        user = User.objects.get(email=request.POST['email'])
    except: 
        messages.error(request, "Please enter a valid registered email")
        return redirect('/')

    password = request.POST['pass']
    if bcrypt.checkpw('password'.encode(), user.password.encode()):
        request.session['email'] = user.email
        return redirect('/home')
    else:
        messages.error(request, "Please enter a valid password")
        return redirect('/')



#### METHOD 2: NORMAL FORM:
def registernormalform(request):
    regform = RegistrationForm(request.POST)

    if regform.is_valid():
        first_name = regform.cleaned_data['first_name']
        last_name = regform.cleaned_data['last_name']
        email = regform.cleaned_data['email']
        birthday = regform.cleaned_data['birthday']
        password = regform.cleaned_data['password']
        hashpass = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        User.objects.create(first_name=first_name, last_name=last_name, email=email, birthday=birthday, password=hashpass)
        request.session['email'] = email
        return redirect('/home')

    return render(request, 'login/index.html', {'regform': regform, 'loginform': LoginForm(),'userform': UserForm() })


def loginnormalform(request):
    loginform = LoginForm(request.POST)

    if loginform.is_valid():
        user = User.objects.get(email=loginform.cleaned_data['email'])
        request.session['email'] = user.email
        return redirect('/home')

    return render(request, 'login/index.html', {'regform': RegistrationForm(), 'loginform': LoginForm(), 'userform': UserForm() })




#### METHOD 3: MODEL FORM:
def registermodelform(request):
    userform = UserForm(request.POST)
    
    if userform.is_valid():
        userform.save()
        request.session['email'] = userform.cleaned_data['email']
        return redirect('/home')
    
    print "form not valid"
    
    return render(request, 'login/index.html', {'regform': RegistrationForm(), 'loginform': LoginForm(), 'userform': userform })

